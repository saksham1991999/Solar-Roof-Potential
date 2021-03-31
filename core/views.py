import os

from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Rooftop
from .serializers import RooftopSerializer
from .utils import get_roof

class SolarRoofPotentialView(viewsets.ModelViewSet):
    queryset = Rooftop.objects.all()
    serializer_class = RooftopSerializer

    # parser_classes = [FileUploadParser]
    """
    List all snippets, or create a new snippet.
    """

    def create(self, request, *args, **kwargs):
        serializer = RooftopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            from core.detector.rooftop import detect
            current_dir = os.getcwd()
            media_dir = os.path.join(current_dir, "media")
            rooftop = get_object_or_404(Rooftop, id = serializer.data["id"])
            image_name = rooftop.image.name
            file = os.path.join(media_dir, image_name)
            area, energy = detect(file)
            rooftop.energy = energy
            rooftop.area = area
            rooftop.save()
            serializer = RooftopSerializer(rooftop, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def location(self, request):
        try:
            lat = request.data['lat']
            lon = request.data['lon']
            solar = request.data['solar']
            image = get_roof(lat, lon)
            rooftop = Rooftop.objects.create(image=image)
            from core.detector.rooftop import detect
            current_dir = os.getcwd()
            media_dir = os.path.join(current_dir, "media")
            image_name = rooftop.image.name
            file = os.path.join(media_dir, image_name)
            area, energy = detect(file)
            rooftop.energy = energy
            rooftop.area = area
            rooftop.save()
            serializer = RooftopSerializer(rooftop, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({"status": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
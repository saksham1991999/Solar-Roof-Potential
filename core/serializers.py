from rest_framework import serializers


from .models import Rooftop


class RooftopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rooftop
        fields = (
            "id",
            "image",
            "area",
            "energy",
            "created_at",
        )
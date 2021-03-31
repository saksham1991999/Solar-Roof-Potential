from django.urls import path
from rest_framework import routers

from . import views

app_name = 'core'

router = routers.SimpleRouter()
router.register(r'rooftops', views.SolarRoofPotentialView)


urlpatterns = [
    # path('', views.SolarRoofPotentialView.as_view(), name='home'),
]

urlpatterns += router.urls
from django.urls import include, path
from rest_framework import routers

from gym.views import GymViewSet, NearbyGymView

router = routers.DefaultRouter()
router.register(r"", GymViewSet, basename="gym")

urlpatterns = [
    path("nearby/", NearbyGymView.as_view(), name="nearby-gym"),
    path("", include(router.urls)),
]

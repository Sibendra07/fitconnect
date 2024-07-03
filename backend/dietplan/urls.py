from django.urls import include, path, re_path
from rest_framework import routers

from dietplan.views import DietPlanViewSet, PredefinedDietPlanViewSet

router = routers.DefaultRouter()
router.register(
    r"predefined", PredefinedDietPlanViewSet, basename="predefined-dietplan"
)

router.register(r"", DietPlanViewSet, basename="dietplan")

urlpatterns = [
    path("", include(router.urls)),
]

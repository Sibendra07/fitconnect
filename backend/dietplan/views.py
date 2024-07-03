from rest_framework import viewsets

from dietplan.models import DietPlan, PredefinedDietPlan
from dietplan.serializers import DietPlanSerializer, PredefinedDietPlanSerializer
from main.views import BaseAuthModelViewSet


class PredefinedDietPlanViewSet(BaseAuthModelViewSet):
    queryset = PredefinedDietPlan.objects.all()
    serializer_class = PredefinedDietPlanSerializer


class DietPlanViewSet(BaseAuthModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

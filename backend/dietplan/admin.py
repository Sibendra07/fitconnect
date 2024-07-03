from django.contrib import admin

from dietplan.models import DietPlan, PredefinedDietPlan


class PredefinedDietPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(PredefinedDietPlan, PredefinedDietPlanAdmin)


class DietPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(DietPlan, DietPlanAdmin)

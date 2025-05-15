from django.contrib import admin
from .models import City, CityTemperature


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(CityTemperature)
class CityTemperatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'value', 'created_at')
    list_filter = ('city', 'created_at')
    search_fields = ('city__name',)

from django.contrib import admin
from .import models

@admin.register(models.Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('type_apartment',)


@admin.register(models.Service)
class ServicetAdmin(admin.ModelAdmin):
    list_display = ('nom',)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('domaine','titre',)



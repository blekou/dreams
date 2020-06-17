from django.urls import path
from .import views

urlpatterns = [
    path('services/', views.services, name="services"),
    path('project/', views.project, name="project"),
    path('apartment/', views.apartment, name="apartment"),
    path('elements/', views.elements, name="elements"),

]
from django.urls import path
from .import views


urlpatterns = [
    path('blog/', views.blog, name="blog"),
    path('single/', views.single, name="single"),
]


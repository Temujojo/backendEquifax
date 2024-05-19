from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs, name="jobs"),
    path('technologies/',views.technologies, name="technologies"),
]

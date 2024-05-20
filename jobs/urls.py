from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.jobs, name="jobs"),
    path('technologies/',views.technologies, name="technologies"),
]

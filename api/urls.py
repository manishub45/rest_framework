from django.urls import path
from .import views


urlpatterns = [
    path('student/', views.get_student, name='get_student')
]

from django.urls import path
from .import views


urlpatterns = [
<<<<<<< HEAD
    path('student/', views.get_student, name='get_student')
=======
    path('student/', views.studentlist, name = 'student-list')
>>>>>>> d5cecdf1f115b278e658bde0392cb98c5ed5e38c
]

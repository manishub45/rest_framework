from django.contrib import admin
from .models import student

# Register your models here.

@admin.register(student)
<<<<<<< HEAD
class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gmail')
    
=======

class studentadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'city']


>>>>>>> d5cecdf1f115b278e658bde0392cb98c5ed5e38c

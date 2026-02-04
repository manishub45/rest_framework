from django.shortcuts import render
<<<<<<< HEAD
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import student
from .serializers import studentSerializers

# Create your views here.

@api_view(['GET'])

def get_student(request):
    students = student.objects.all()
    serializers = studentSerializers(students, many=True)
    return Response(serializers.data)
=======
from rest_framework.decorators import api_view
from .models import student
from .Serializers import studentserializers
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])

def studentlist(request):
    students = student.objects.all()
    serializer = studentserializers(students, many=True)
    return Response(serializer.data)


>>>>>>> d5cecdf1f115b278e658bde0392cb98c5ed5e38c

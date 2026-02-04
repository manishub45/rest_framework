from django.shortcuts import render
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

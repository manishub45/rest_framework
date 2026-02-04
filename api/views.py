from django.shortcuts import render
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



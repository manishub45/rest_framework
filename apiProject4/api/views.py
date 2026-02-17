from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


                    #    BASIC AUHENTICATION AND AllowAny AND IsAuthenticated

@api_view(['GET'])
@permission_classes([AllowAny])

def public_view(request):
    return Response({"message":"this is public api"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])

def private_view(request):
    return Response(f"hello, {request.user.username}.this is private api")
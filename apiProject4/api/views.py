# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny


#                     #    BASIC AUHENTICATION AND AllowAny AND IsAuthenticated

# @api_view(['GET'])
# @permission_classes([AllowAny])

# def public_view(request):
#     return Response({'message' : "this is public api"})


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])

# def private_view(request):
#     return Response(f'hello {request.user.username}. this is private api')


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializers
from rest_framework import status


@api_view(['GET', 'POST'])
def blog_list(request):

    # GET → saare blogs fetch
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializers(blogs, many=True)
        return Response(serializer.data)

    # POST → naya blog create
    elif request.method == 'POST':
        serializer =BlogSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

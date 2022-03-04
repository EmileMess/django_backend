from django.shortcuts import render

from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        print("GET: ", serializer.data)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            print("Got POST request")
            allimages = request.FILES.getlist('images')
            for image in allimages:
                Post.objects.create(images=image)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
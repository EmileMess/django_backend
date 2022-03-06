from contextlib import nullcontext
from unicodedata import name
from .serializers import PostSerializer, DatasetSerializer, ImageSerializer
from .models import Post, Dataset, Image
from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # TODO: Errors in console
    # TODO: Tokens!
    # TODO: params "email" und "datasetname" aus react nicht local

    def get(self, request, *args, **kwargs):
        images = Image.objects.get(dataset = Dataset.objects.get(name="yy", user=CustomUser.objects.get(email="e.mess1806@gmail.com")))
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            allimages = request.FILES.getlist('images')
            datasetname = request.POST.get('datasetname')
            useremail = request.POST.get('user')
            if Dataset.objects.filter(name=datasetname, user=CustomUser.objects.get(email=useremail)).exists():
                return Response(status=status.HTTP_403_FORBIDDEN)
            Dataset.objects.create(name=datasetname, user=CustomUser.objects.get(email=useremail))
            for image in allimages:
                Image.objects.create(name='img', image=image, dataset=Dataset.objects.get(name=datasetname, user=CustomUser.objects.get(email=useremail)))
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
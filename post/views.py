from .serializers import PostSerializer, DatasetSerializer, ImageSerializer
from .models import Post, Dataset, Image
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # def get(self, request, *args, **kwargs):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         allimages = request.FILES.getlist('images')
    #         for image in allimages:
    #             Post.objects.create(images=image)
    #         return Response(status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)



    def get(self, request, *args, **kwargs):
        datasets = Dataset.objects.all()
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            allimages = request.FILES.getlist('images')
            datasetname = "mydataset"
            user = "myuser"
            # dataset = Dataset.objects.get(datasetname=datasetname, user=user)
            dataset = Dataset.objects.create(datasetname=datasetname, user=user)
            for image in allimages:
                Image.objects.create(name='img', image=image, dataset=dataset)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
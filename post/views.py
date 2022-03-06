from contextlib import nullcontext
from unicodedata import name
from .serializers import DatasetSerializer, ImageSerializer
from .models import Dataset, Image
from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status


class uploadDataView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # TODO: Favicon
    # TODO: Errors in console
    # TODO: Tokens!

    # get all datasets
    def get(self, request):
        datasets = Dataset.objects.all()
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data)

    # upload one dataset
    def post(self, request):
        if request.method == "POST":
            allimages = request.FILES.getlist('images')
            datasetname = request.POST.get('datasetname')
            useremail = request.POST.get('user')
            user = CustomUser.objects.get(email=useremail)

            # Check if dataset already exists
            if Dataset.objects.filter(name=datasetname, user=user).exists():
                return Response(status=status.HTTP_403_FORBIDDEN)
            
            # Create new dataset and fill data
            dataset = Dataset.objects.create(name=datasetname, user=user)
            for image in allimages:
                Image.objects.create(name='img', image=image, dataset=dataset)

            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class getImagesView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # TODO: params "email" und "datasetname" aus react nicht local

    # get images from one dataset
    def get(self, request):
        user = CustomUser.objects.get(email=request.query_params["user"])
        datasetname = request.query_params["datasetname"]
        dataset = Dataset.objects.filter(name=datasetname, user=user)

        # serializer = DatasetSerializer(dataset, many=True)
        # return Response(serializer.data)

        images = Image.objects.filter(dataset=dataset)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
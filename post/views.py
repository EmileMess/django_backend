from contextlib import nullcontext
from unicodedata import name
from .serializers import DatasetSerializer, ImageSerializer
from .models import Dataset, Image
from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .AI.main import augment_images

# TODO: Create unique file name when saving images
# TODO: Create container for each user
# TODO: Delete dataset
# TODO: Access control


class runAugmentation(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        images = getAllImages(request)
        result = augment_images(images)

        # Save new augmented dataset
        # frame_jpg = cv2.imencode('.jpg', array)
        # file = ContentFile(frame_jpg)
        # instance.photo.save('myphoto.jpg', file, save=True)
        return Response(result)


class uploadDataView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # get datasets with first_image and img_num each
    def get(self, request):
        user = CustomUser.objects.get(email=request.query_params["user"])
        datasets = Dataset.objects.filter(user=user)
        
        if not datasets.exists():
            return Response(status=status.HTTP_409_CONFLICT)

        result = []

        for dset in datasets:
            images = Image.objects.filter(dataset=dset)
            data_serializer = DatasetSerializer(dset)
            image_serializer = ImageSerializer(images[0])
            mydict = {'img_num': len(images), 'img_first': image_serializer.data["image"]}
            mydict.update(data_serializer.data)
            result.append(mydict)

        return Response(result)

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

    def get(self, request):
        result = getAllImages(request)
        return Response(result)


#############################


# get images from one dataset
def getAllImages(request):
    user = CustomUser.objects.get(email=request.query_params["user"])
    datasetname = request.query_params["datasetname"]

    # Check if Dataset exists
    dataset = Dataset.objects.filter(name=datasetname, user=user) # Should be only one dataset - Why is get() not working?
    if not dataset.exists():
        return Response(status=status.HTTP_409_CONFLICT)

    images = Image.objects.filter(dataset=dataset[0])
    serializer = ImageSerializer(images, many=True)
    return serializer.data

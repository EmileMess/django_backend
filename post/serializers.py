from rest_framework import serializers
from .models import Dataset, Image

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'



class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
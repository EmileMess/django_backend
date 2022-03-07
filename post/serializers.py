from rest_framework import serializers
from .models import Dataset, Image


class DatasetSerializer(serializers.ModelSerializer):

    img_first = serializers.SerializerMethodField()
    img_num = serializers.SerializerMethodField()

    class Meta:
        model = Dataset
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
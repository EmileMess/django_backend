from django.db import models
from users.models import CustomUser

# Create your models here.

# class Post(models.Model):
#     images = models.FileField(upload_to='data', default='')


class Dataset(models.Model):
    name = models.CharField(default='', max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Image(models.Model):
    name = models.CharField(default='', max_length=100)
    image = models.FileField(upload_to='data', default='')
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
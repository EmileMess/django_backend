from django.db import models

# Create your models here.

class Post(models.Model):
    images = models.FileField(upload_to='media/datasets', default='')
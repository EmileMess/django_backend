from django.urls import path
from . import views

urlpatterns = [
    path('uploadDataset/', views.uploadDataView.as_view(), name= 'uploadDataset'),
    path('getImages/', views.getImagesView.as_view(), name= 'getImages'),
    path('runAugmentation/', views.runAugmentation.as_view(), name= 'runAugmentation'),
]
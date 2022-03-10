import numpy as np
from PIL import Image
from urllib import request
from io import BytesIO

def process_images (images):
    np_images = []
    for img in images:
        im = np.rot90(np.asarray(Image.open(BytesIO(request.urlopen(img['image']).read()))))
        np_images.append(im)
    return np_images

def augment_images(images):
    processed_images = process_images(images)
    return processed_images
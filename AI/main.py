import numpy as np
import skimage

def process_images (images):
    np_images = []
    for img in images:
        im = skimage.io.imread(img['image'])
        im = np.rot90(im)
        np_images.append(im)
    return np_images

def augment_images(images):
    processed_images = process_images(images)
    return processed_images
from PIL import Image
from urllib import request
from io import BytesIO
import numpy as np

url = 'https://backenddjangostorage.blob.core.windows.net/media/data/000000000009.jpg'

im = np.rot90(np.asarray(Image.open(BytesIO(request.urlopen(url).read()))))

print(im)
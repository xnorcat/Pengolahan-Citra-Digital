# importing required libraries
import mahotas as mh
import numpy as np
from pylab import imshow, show

# creating region
# numpy.ndarray
daerah = np.zeros((10, 10), bool)

# setting 1 value to the region
daerah[1, :4] = 1
daerah[1:8, 6: 10] = 1
daerah[4, 0] = 1

# showing the image with interpolation = 'nearest'
print("Gambae")
imshow(daerah, interpolation ='nearest')
show()

# template for hit miss
template = np.array([
            [0, 1, 1],
            [0, 1, 1],
            [0, 1, 1]])

# hit miss transform
gambar = mh.hitmiss(daerah, template)

# showing image
print("Gambar setelah transformasi hit miss")
imshow(gambar)
show()

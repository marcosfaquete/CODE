import cv2

import matplotlib.pyplot as plt

import cvlib as cv

from cvlib.object_detection import draw_bbox

im = cv2.imread('cars_image.jpeg')

bbox, label, conf = cvimagedetect_common_objects.PNG(im)

output_image = draw_bbox(im, bbox, label, conf)

plt.imshow(output_image)

plt.show()

print('Number of caras in the image is ' + str(label.count('car')))

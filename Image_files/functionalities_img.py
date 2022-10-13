''' Cropping, rotating and translation of image'''
import cv2
import numpy as np
img = cv2.imread('./Image_Samples/butterfly.jpeg')
height, width, channel = img.shape
# Cropping of image
# cropped_img = img[start_row:end_row, start_col:end_col]
cropped_img = img[70:260, 130:350]


# Rotation of image
r_matrix = cv2.getRotationMatrix2D((width/2,height/2), 10, 1)
rotated_img = cv2.warpAffine(img, r_matrix, (width,height))

# Translation of image
t_matrix = np.float32([[1,0,100],[0,1,100]])
translate_img = cv2.warpAffine(img, t_matrix, (width,height))

cv2.imshow('cropped_image', cropped_img)
cv2.imshow('rotated_image', rotated_img)
cv2.imshow('image', img)
cv2.imshow('translated_image', translate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

# color format
# ! specify the path according to you

img = cv2.imread('./OpenCV-Tutorial/Image_Samples/butterfly.jpeg', 1)
# greyscale format
img2 = cv2.imread('./OpenCV-Tutorial/Image_Samples/butterfly.jpeg', 0)

cv2.imshow('image', img2)
cv2.waitKey(0)

cv2.imwrite('./OpenCV-Tutorial/Image_Samples/grey_butterfly.jpg', img2)

cv2.destroyAllWindows()
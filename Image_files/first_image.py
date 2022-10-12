import cv2

# ! specify the path according to you

# color format
# img = cv2.imread('./Image_Samples/butterfly.jpeg', 1)
# greyscale format
img2 = cv2.imread('./Image_Samples/butterfly.jpeg', 0)

# cv2.imshow('image', img)
cv2.imshow('image1', img2)

k = cv2.waitKey(0)

# if escape is pressed then destroy windows, s is pressed then save the image
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('./Image_Samples/grey_butterfly.jpg', img2)
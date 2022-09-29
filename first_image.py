import cv2

# color format
img = cv2.imread('D:/Python programs/OpenCV Tutorial/butterfly.jpeg', 1)
# greyscale format
img2 = cv2.imread('./OpenCV Tutorial/butterfly.jpeg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)

cv2.imwrite('./OpenCV Tutorial/grey_butterfly.jpg', img2)

cv2.destroyAllWindows()
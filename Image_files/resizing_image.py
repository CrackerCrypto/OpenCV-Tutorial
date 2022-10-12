import cv2

img = cv2.imread('./Image_Samples/butterfly.jpeg')

cv2.imshow('Original Image', img)

# print(img.shape)
# print(type(img.shape))

#! unpack the tuple
h,w,c = img.shape
print('OG width and height:', w,"x",h)
print("number of channels: ", c)

# Resizing the image
up_width = 700
up_height = 500
new_size = (up_width, up_height)
resized_up = cv2.resize(img, new_size, interpolation = cv2.INTER_LINEAR)

# cv2.imshow('Sized Up Image', resized_up)

# scaling factor
scale_up = 1.2
scale_down = 0.6

scale_up_img = cv2.resize(img, None, fx=scale_up, fy=scale_up, interpolation = cv2.INTER_LINEAR)
cv2.imshow("Scaled Up Image", scale_up_img)

scale_down_img = cv2.resize(img, None, fx=scale_down, fy=scale_down, interpolation = cv2.INTER_LINEAR)
cv2.imshow("Scaled down Image", scale_down_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
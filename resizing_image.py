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

cv2.imshow('Sized Up Image', resized_up)

cv2.waitKey(0)
cv2.destroyAllWindows()
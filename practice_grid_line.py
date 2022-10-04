''' This is a practice file where gridlines are created using cv2.line() 
P.S - Only for practice...'''
import cv2

img = cv2.imread('./Image_Samples/butterfly.jpeg')

img_height = img.shape[0]
img_width = img.shape[1]

# print(img_height,img_width)

Y = img_height//3
X = img_width//3

for y in range(0, img_height, Y):
    for x in range(0, img_width, X):
        if (img_height - y) < Y or (img_width - x)< X:
            break

        y1 = y + Y
        x1 = x + X
        
        # y1 = 0+111=111
        # x1 = 0+166=166
        
        cv2.line(img, (x1,0), (x1,img_height),(0,0,255), 1)
        cv2.line(img, (0,y1), (img_width,y1), (0,0,255), 1)


cv2.imshow('Grid Image', img)

cv2.imwrite('./Image_Samples/Grid-Picture.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
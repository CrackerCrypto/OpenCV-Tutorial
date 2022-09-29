import numpy as np
import cv2

# img_path = './OpenCv Tutorial/butterfly.jpeg'
# img = cv2.imread(img_path, 1)

img = np.zeros([480,640,3], np.uint8)

cv2.line(img, (20,100),(40,150),(0, 0, 255), 4)
cv2.arrowedLine(img, (100,100),(40,255),(0, 0, 255), 4)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, 'Hello!', (0,100), font, 4, (255,0,255), 3, cv2.LINE_AA)


cv2.imshow('Picture', img)

cv2.imwrite('./OpenCV Tutorial/Geometry.jpeg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
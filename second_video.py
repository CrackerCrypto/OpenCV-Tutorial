'''Playing video from resources'''
import cv2
from cv2 import CAP_PROP_FPS
from cv2 import CAP_PROP_FRAME_COUNT

footage = cv2.VideoCapture('./OpenCV-Tutorial/Resources/Street - 19627.mp4')
if footage.isOpened() == False:
    print('There is an error in playing')
else:
    # get() retrieves the meta-data about the video
    fps = int(footage.get(CAP_PROP_FPS))
    print('Frames per second: ',fps)

    frame_count = int(footage.get(CAP_PROP_FRAME_COUNT))
    print('Frame count: ', frame_count)

while footage.isOpened():
    ret, frame = footage.read()

    if ret == True:
        cv2.imshow('Video', frame)
'''Playing video from resources'''
import cv2
from cv2 import CAP_PROP_FPS
from cv2 import CAP_PROP_FRAME_COUNT
from cv2 import CAP_PROP_FRAME_WIDTH
from cv2 import CAP_PROP_FRAME_HEIGHT

footage = cv2.VideoCapture('./Resources/Street - 19627.mp4')
if footage.isOpened() == False:
    print('There is an error in playing')
else:
    # get() retrieves the meta-data about the video
    fps = int(footage.get(CAP_PROP_FPS))
    print('Frames per second: ',fps)

    frame_count = int(footage.get(CAP_PROP_FRAME_COUNT))
    print('Frame count: ', frame_count)

    frame_width = int(footage.get(CAP_PROP_FRAME_WIDTH))
    print("Frame width: ", frame_width)

    frame_height = int(footage.get(CAP_PROP_FRAME_HEIGHT))
    print("Frame height: ", frame_height)

while footage.isOpened():
    ret, frame = footage.read()

    if ret == True:
        cv2.imshow('Video', frame)
        k = cv2.waitKey(20)
        # when q is pressed the window will close
        if k == ord('q'):
            break
    else:
        break

footage.release()
cv2.destroyAllWindows()
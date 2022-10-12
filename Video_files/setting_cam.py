''' Setting the camera parameters and also writing on the frame'''

import cv2
import datetime as dt
footage = cv2.VideoCapture(0)

width = footage.get(cv2.CAP_PROP_FRAME_WIDTH)
height = footage.get(cv2.CAP_PROP_FRAME_HEIGHT)

#* usage of set()
# footage.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# footage.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# print(footage.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(footage.get(cv2.CAP_PROP_FRAME_HEIGHT))

while footage.isOpened():
    ret, frame = footage.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width:' + str(width) + ' ' + 'Height: ' + str(height)

        ''' There are 2 ways of showing the date&time on the video. 
            One: simply convert it using str() and then print, but it will show millieseconds too.
            Two: use strftime("%d-%m-%Y %H:%M:%S").[This one is optional/technical]
        '''

        datet = dt.datetime.now()
        dt_string = datet.strftime("%d-%m-%Y %H:%M:%S")
        frame = cv2.putText(frame, dt_string, (10, 50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF ==27:
            break
    else:
        break

footage.release()
cv2.destroyAllWindows()
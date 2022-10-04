import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./output.mp4', fourcc, 20.0, (640,480))

while True:
    # ret holds a boolean value, if frame is created then True otherwise False
    ret, frame = cap.read()

    cv2.imshow('OUTPUT',frame)

    if ret == True:
        # write() is used to save the video
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
    
#releasing the allocated resources
cap.release()
out.release()
cv2.destroyAllWindows()

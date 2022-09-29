import cv2

cap =  cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # * for normal video
    # cv2.imshow('Frame', frame)
    
    # Video in grayscale
    gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)

    # width and height of the frame
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


    # !here 27 represents the Esc key
    #? The reasons behind passing 1 as the argument in waitKey() because it will continuously render video, 
    #? but if 0 is passed the we have to press a key so that the video can render

    if cv2.waitKey(1) & 0xFF == 27:
        break

# release the all allocated resources
cap.release()
cv2.destroyAllWindows()
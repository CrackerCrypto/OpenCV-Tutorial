# OpenCV-Tutorial
Keeping a track of everything
FOR IMAGE PART:
------------------------
-> Cropping an image is somewhat similar to slicing an array. So, to slice an array we need to know about starting index and ending index as well.
-> Translation of an image...
-> Rotation of an image...

FOR VIDEO PART:
------------------------
Fourcc - Fourcc stands for four character code defines the video codec of a media file. Fourcc is a 32bit ASCII character
code where each character is having 8bits.
    A video codec is a software or hardware for compressing or decompressing a digital video.

get(PROPERTY_NAME) is a method in VideoCapture which fetches all the meta data about any video file.
set(PROPERTY_NAME, value) is a method in VideoCapture which set the desired property with the value given.

Properties:
------------------------
    => CAP_PROP_FPS returns the number of frames per second of a video
    => CAP_PROP_FRAME_COUNT returns the frame count
    => CAP_PROP_FRAME_WIDTH returns the frame width
    => CAP_PROP_FRAME_HEIGHT return the frame height
import cv2
import sys

# Get user supplied values
cascPath = sys.argv[1]
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# initialize the camera
usb_camera = cv2.VideoCapture(0)
usb_camera.set(3,160) #video capture height
usb_camera.set(4,120) #video capture width

while True:
    # Capture frame by frame
    ret, frame = usb_camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done just release the capture
usb_camera.release()
cv2.destroyAllWindows()

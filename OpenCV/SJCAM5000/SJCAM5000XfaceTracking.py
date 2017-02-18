import cv2
import numpy as np

# Get user supplied values
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
streamUri = "rtsp://192.168.1.254/live/ch0"

# initialize the camera
cap = cv2.VideoCapture(streamUri) # capture from SJCAM 5000X
thickness = 2

while True:
    # Capture frame by frame
    if not (cap.isOpened()):
        cap.open(streamUri)
    ret, frame = cap.read()
    if (ret == True):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        for (x, y, w, h) in faces:
            face_roi_gray = gray[y:y + h, x:x + w]
            eyes = eyeCascade.detectMultiScale(face_roi_gray)
            if len(eyes) >= 1:
                Cx = (int)(x + w / 2)
                Cy = (int)(y + h / 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness)
                #cv2.circle(frame, (Cx, Cy), 5, (0, 255, 0), -1)
                centerCoordinatesStr = str(Cx) + ', ' +str(Cy)
                cv2.putText(frame, centerCoordinatesStr, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), thickness)

    # Display the resulting frame
    cv2.imshow('SJCAM5000X Face Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif (ret == False):
        print("No Frame")

# When everything is done just release the capture
cap.release()
cv2.destroyAllWindows()
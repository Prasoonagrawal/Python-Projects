import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascase=cv2.CascadeClassifier('haarcascade_eye.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        roi_gray=gray[y:y+h,x:x+w]
        roi_colot=img[y:y+h,x:x+w]
        eye=eye_cascase.detectMultiScale(roi_gray,1.3,5)
        for(ex,ey,eh,ew) in eye:
            cv2.rectangle(roi_colot,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


    cv2.imshow('img', img)

    # Stop if escape key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release the VideoCapture object
cap.release()

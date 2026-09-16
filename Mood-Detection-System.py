import cv2

face_cascade = cv2.CascadeClassifier("/home/ankit/projects/MOOD DETECTION/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/ankit/projects/MOOD DETECTION/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("/home/ankit/projects/MOOD DETECTION/haarcascade_smile.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    """
    detectMultiScale() - scan & detect faces
    1.1 balance, not too slow, blind
    
    minNeighbors = 5
    """

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

        """
        x,y - top left corner
        
        (x+w, y+h)
        
        fcae = [
        (100, 150, 80, 80) face1
        (200, 120, 90, 90) face2
        ]
        x - how far from left
        y - how far from the top
        w - width of the face
        h - height of the face
        """

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(eyes) > 0:
            cv2.putText(frame, "Smile Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    cv2.imshow("Webcame Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
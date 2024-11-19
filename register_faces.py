import cv2
import dlib
import os
import pickle
import numpy as np

# Initialize dlib's face detector and face recognizer
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

# Directory to store faces
if not os.path.exists('dataset'):
    os.makedirs('dataset')

# Function to capture and store face encodings
def capture_face_encoding():
    cap = cv2.VideoCapture(0)
    
    print("Please look at the camera and enter your name when prompted.")
    name = input("Enter your name: ")

    face_encodings = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(frame)
        
        for face in faces:
            shape = sp(frame, face)
            encoding = facerec.compute_face_descriptor(frame, shape)
            face_encodings.append(encoding)
            
            # Debugging: print encoding size and show the face
            print(f"Encoding for {name}: {len(encoding)} values")
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
        
        cv2.putText(frame, "Press 's' to save or 'q' to quit.", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f'Name: {name}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Capturing Face", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Save the encoding to a pickle file
            if face_encodings:
                with open('known_faces.pkl', 'ab') as f:
                    pickle.dump((name, face_encodings), f)
                print("Encoding saved!")
            else:
                print("No face detected. Please try again.")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

capture_face_encoding()

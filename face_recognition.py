import cv2
import dlib
import os
import pickle
import numpy as np
import csv
from datetime import datetime

# Initialize dlib's face detector and face recognizer
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

# Load known faces and names
def load_known_faces():
    known_faces = []
    known_names = []
    try:
        with open('known_faces.pkl', 'rb') as f:
            while True:
                try:
                    name, encodings = pickle.load(f)
                    known_faces.append(encodings)
                    known_names.append(name)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No registered faces found.")
    return known_faces, known_names

known_faces, known_names = load_known_faces()

# Function to check if attendance is already logged for the day
def is_logged_today(name):
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        with open('attendance.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name and row[1].startswith(today):  # Check if name and today's date match
                    return True
    except FileNotFoundError:
        return False
    return False

# Function to store attendance in CSV file
def log_attendance(name):
    today = datetime.now().strftime("%Y-%m-%d")
    
    if is_logged_today(name):
        print(f"Attendance for {name} is already recorded today.")
        return  # Skip if already logged for today
    
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('attendance.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date_time])  # Write name and timestamp
    print(f"Attendance for {name} recorded on {today}.")

# Function to recognize a face and store attendance
def recognize_face():
    cap = cv2.VideoCapture(0)
    print("Starting face recognition...")

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

            # Compare with known faces
            distances = []
            for known_face in known_faces:
                for known_encoding in known_face:
                    dist = np.linalg.norm(np.array(known_encoding) - np.array(encoding))
                    distances.append(dist)

            # Find the minimum distance and compare with a threshold
            if distances:
                min_distance = min(distances)
                print(f"Min distance: {min_distance}")
                if min_distance < 0.6:  # Adjust this threshold if necessary
                    index = distances.index(min_distance)
                    name = known_names[index // len(known_faces[0])]
                    cv2.putText(frame, f"Hello {name}!", (face.left(), face.top() - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    
                    # Log attendance for the recognized person
                    log_attendance(name)
                else:
                    cv2.putText(frame, "Unknown", (face.left(), face.top() - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    
            # Draw rectangle around face
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
        
        cv2.imshow("Face Recognition", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

recognize_face()

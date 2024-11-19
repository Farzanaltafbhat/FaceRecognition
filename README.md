# Face Recognition Attendance System

This is a simple **Face Recognition Attendance System** built using Python, OpenCV, and Flask. The system captures attendance by recognizing faces from a webcam, and logs the attendance with the timestamp to a CSV file. The backend is implemented in Flask, and the frontend can be integrated using simple HTML and JavaScript.

## Project Requirements

### Prerequisites

- Python 3.x
- Libraries:
  - `opencv-python`
  - `flask`
  - `face_recognition`
  - `pandas`
  - `numpy`
  - `dlib` (Optional, for better face recognition performance)

You can install the required libraries using:

```bash
pip install -r requirements.txt
git clone https://github.com/yourusername/FaceRecognition.git
cd FaceRecognition

#Run the Flask Backend

python app.py

#Make sure to run register_faces.py first to register the face using

```bash
python register_faces.py

#Then use the face_recognition.py
```bash
python face_recognition.py

#After getting the backend running App.py
#Run the Index.html in a browser to see the attendance data


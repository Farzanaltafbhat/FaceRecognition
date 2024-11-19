# Face Recognition Attendance System

This is a simple **Face Recognition Attendance System** built using Python, OpenCV, and Flask. The system captures attendance by recognizing faces from a webcam and logs the attendance with the timestamp to a CSV file. The backend is implemented in Flask, and the frontend can be integrated using simple HTML and JavaScript.

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
Clone the Repository
To clone the repository:

bash
Copy code
git clone https://github.com/yourusername/FaceRecognition.git
cd FaceRecognition
Running the Application
1. Install Dependencies
Before running the system, make sure you have installed all dependencies by running:

bash
Copy code
pip install -r requirements.txt
2. Register Faces
To register faces for recognition, run the register_faces.py script. This will prompt you to capture face images for each individual.

bash
Copy code
python register_faces.py
Make sure that the images directory is populated with the registered faces for each individual.

3. Run Face Recognition
Once the faces are registered, you can start the face recognition system by running the face_recognition.py script. This script will continuously monitor the webcam for recognized faces and log the attendance with timestamps.

bash
Copy code
python face_recognition.py
4. Run the Flask Backend
After setting up face recognition, run the Flask backend server to manage attendance data. This will expose the API at http://127.0.0.1:5000 for the frontend to interact with.

bash
Copy code
python app.py
5. View Attendance Data in the Frontend
Once the Flask backend is running, you can view the attendance data in your browser by running the Index.html file. The HTML file will fetch the attendance data from the backend and display it in a table.

Simply open Index.html in your browser to view the real-time attendance data.

Contributing
If you'd like to contribute to the project, feel free to fork it, make changes, and submit a pull request. Suggestions, bug reports, and feature requests are welcome!

License
This project is open source and available under the MIT License.

Acknowledgements
OpenCV: For video capture and face recognition.
face_recognition: Python library for facial recognition.
Flask: For the backend API.
Thanks to all contributors who help improve this project!
vbnet
Copy code

### Changes:

1. Commands are now listed as distinct sections with headings.
2. The `register_faces.py`, `face_recognition.py`, and `app.py` steps are now clarified in separate numbered sections to make them easy to follow.
3. A clearer structure to the steps of running the project and interacting with the frontend and backend.

This structure should be easier to follow and more professional. Let me know if you'd like any more adjustments!






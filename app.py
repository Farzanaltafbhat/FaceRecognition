from flask import Flask, jsonify
import csv
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to read attendance data from CSV file
def read_attendance():
    attendance_data = []
    try:
        with open('attendance.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                attendance_data.append({"name": row[0], "timestamp": row[1]})
    except FileNotFoundError:
        return []
    return attendance_data

@app.route('/attendance', methods=['GET'])
def get_attendance():
    attendance_data = read_attendance()
    return jsonify(attendance_data)

if __name__ == '__main__':
    app.run(debug=True)

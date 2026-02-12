from fastapi import FastAPI
import qrcode
import uuid
from datetime import datetime

app = FastAPI()

sessions = {}
attendance_register = []

# ===============================
# HOME
# ===============================
@app.get("/")
def home():
    return {"message": "Smart Classroom Attendance Running"}

# ===============================
# 1️⃣ TEACHER START CLASS
# ===============================
@app.post("/start-class")
def start_class(
    school_name: str,
    teacher_name: str,
    subject: str,
    period: int,
    total_students: int
):
    session_token = str(uuid.uuid4())

    qr = qrcode.make(session_token)
    file_name = f"{session_token}.png"
    qr.save(file_name)

    sessions[session_token] = {
        "school": school_name,
        "teacher": teacher_name,
        "subject": subject,
        "period": period,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "total_students": total_students
    }

    return {
        "message": "Class Started",
        "qr_token": session_token,
        "qr_image": file_name
    }

# ===============================
# 2️⃣ MARK STUDENT ATTENDANCE
# ===============================
@app.post("/mark-attendance")
def mark_attendance(
    qr_token: str,
    student_name: str,
    roll_number: str,
    status: str   # Present / Absent
):
    if qr_token not in sessions:
        return {"error": "Invalid Session"}

    class_data = sessions[qr_token]

    record = {
        "school": class_data["school"],
        "teacher": class_data["teacher"],
        "subject": class_data["subject"],
        "period": class_data["period"],
        "date": class_data["date"],
        "student_name": student_name,
        "roll_number": roll_number,
        "status": status
    }

    attendance_register.append(record)

    return {"message": "Attendance Added"}

# ===============================
# 3️⃣ VIEW FULL ATTENDANCE SHEET
# ===============================
@app.get("/attendance-sheet")
def view_attendance():
    return attendance_register

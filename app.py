import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🏫 Smart Attendance System")

# =========================
# START CLASS SECTION
# =========================
st.header("📚 Start Class")

school = st.text_input("School Name")
teacher = st.text_input("Teacher Name")
subject = st.selectbox("Subject", ["Tamil","English","Maths","Science","Social"])
period = st.number_input("Period", 1, 8)

if st.button("Start Class"):
    url = f"{API_URL}/start-class?school_name={school}&teacher_name={teacher}&subject={subject}&period={period}&total_students=0"
    res = requests.post(url).json()
    st.session_state["token"] = res["qr_token"]
    st.success("Class Started Successfully")

# =========================
# ADD STUDENTS SECTION
# =========================
st.header("🧑‍🎓 Mark Attendance")

if "students" not in st.session_state:
    st.session_state.students = []

name = st.text_input("Student Name")
roll = st.text_input("Roll Number")

col1, col2 = st.columns(2)

if col1.button("Present"):
    if "token" in st.session_state:
        url = f"{API_URL}/mark-attendance?qr_token={st.session_state.token}&student_name={name}&roll_number={roll}&status=Present"
        requests.post(url)
        st.success("Marked Present")

if col2.button("Absent"):
    if "token" in st.session_state:
        url = f"{API_URL}/mark-attendance?qr_token={st.session_state.token}&student_name={name}&roll_number={roll}&status=Absent"
        requests.post(url)
        st.error("Marked Absent")

# =========================
# VIEW ATTENDANCE
# =========================
st.header("📊 Attendance Sheet")

if st.button("Load Attendance"):
    data = requests.get(f"{API_URL}/attendance-sheet").json()
    st.table(data)

# 🏫 Smart Attendance Management System

A Streamlit + FastAPI based Smart Classroom Attendance System that allows teachers to start a class, mark attendance for multiple students, and view attendance reports in real-time.

---

## 🚀 Features

- Start classroom session  
- Add multiple students attendance  
- Present / Absent marking  
- Subject & Period tracking  
- Teacher & School details  
- Automatic date & time recording  
- Attendance report table  
- Streamlit Dark Theme UI  
- FastAPI backend integration  

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- Requests
- QRCode Library
- Git & GitHub

---

## 📂 Project Structure
```
Smart-Attendance-System/
│
├── backend/
│ ├── main.py
│ └── init.py
│
├── .streamlit/
│ └── config.toml
│
├── app.py
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone Repository
```
git clone https://github.com/huzma-nova/smart-attendance-system.git

cd smart-attendance-system
```
### 2. Install Requirements
```
pip install fastapi uvicorn streamlit requests qrcode geopy
```

### 3. Run Backend Server
```
python -m uvicorn backend.main:app --reload

```


FastAPI will run at:
    ```
    http://127.0.0.1:8000/docs
    ```
### 4. Run Streamlit App

Open new terminal:
     ```
     streamlit run app.py
     ```
     
Streamlit will run at:
     ```
     http://localhost:8501
     ```

     
---

## 🧑‍🏫 How to Use

### Start Class
1. Enter School Name  
2. Enter Teacher Name  
3. Select Subject  
4. Select Period  
5. Click **Start Class**

### Mark Attendance
1. Enter Student Name & Roll Number  
2. Click **Present** or **Absent**  
3. Repeat for multiple students

### View Report
Click **Load Attendance** to see attendance sheet.

---

## 📊 Sample Output

| Roll No | Student Name | Subject | Status |
|--------|--------------|--------|--------|
| 01 | Arjun | Maths | Present |
| 02 | Meena | Maths | Absent |
| 03 | Ravi | Maths | Present |

---

## 🎯 Future Enhancements

- Export attendance to Excel  
- Charts & analytics  
- Database integration  
- QR code student scanning  
- Login authentication  

---
## 📸 Screen shot

<img width="532" height="583" alt="image" src="https://github.com/user-attachments/assets/44ff81b2-beea-4de7-95d8-8e536540d933" />

---

## 👩‍💻 Author

Huzma A

Python developer

🔗linkedin link-https://www.linkedin.com/in/a-huzma/

---

⭐ If you like this project, give it a star on GitHub!





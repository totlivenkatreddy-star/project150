from fastapi import FastAPI
from database import Base, engine
from models import Student

app = FastAPI()
students = [{"name":"venkat"}]  
Base.metadata.create_all(bind=engine)

@app.get("/")
def get_students():
    return {"welcome ": "To the home page"}

@app.post("/students")
def add_student(student: dict):
    students.append(student)
    return {"message": "Student added", "data": student}


@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id < len(students):
        return students[student_id]
    return {"error": "Student not found"}

@app.put("/students/{student_id}")
def update_student(student_id: int, student: dict):
    if student_id < len(students):
        students[student_id] = student
        return {"message": "Updated successfully"}
    return {"error": "Student not found"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id < len(students):
        students.pop(student_id)
        return {"message": "Deleted successfully"}
    return {"error": "Student not found"}
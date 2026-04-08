from fastapi import FastAPI

from schemas.course_schema import CourseCreate
from schemas.user_schema import UserCreate
from services import user_service

app = FastAPI()

@app.post("/add-facilitator")
async def create_facilitator(facilitator : UserCreate):
    return user_service.create_facilitator(facilitator)

@app.get("/facilitators/all")
async def get_facilitators():
    return user_service.get_facilitators()

@app.post("/add-student")
async def create_student(student : UserCreate):
    return user_service.create_student(student)

@app.get("/students/all")
async def get_students():
    return user_service.get_students()

@app.post("/create-course")
async def create_course(course : CourseCreate):
    return user_service.create_course(course)
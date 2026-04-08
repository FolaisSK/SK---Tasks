from fastapi import APIRouter

from models.enrollment import Enrollment
from schemas.course_schema import CourseCreate
from schemas.enrollment_schema import AssignGradeSchema
from schemas.user_schema import UserCreate
from services import user_service, enrollment_service

router = APIRouter(prefix="/app", tags=["Student Course Management System"])

@router.post("/add-facilitator")
async def create_facilitator(facilitator : UserCreate):
    return  user_service.create_facilitator(facilitator)

@router.get("/facilitators/all")
async def get_facilitators():
    return user_service.get_facilitators()

@router.post("/add-student")
async def create_student(student : UserCreate):
    return user_service.create_student(student)

@router.get("/students/all")
async def get_students():
    return user_service.get_students()

@router.post("/create-course")
async def create_course(course : CourseCreate):
    return user_service.create_course(course)

@router.get("/view-facilitator")
async def view_facilitator(user_id : str):
    return user_service.find_facilitator(user_id)

@router.get("/view-student")
async def view_student(user_id : str):
    return user_service.find_student(user_id)

@router.post("/enroll-student")
async def enroll_student(course_id : str, student_id : str):
    return enrollment_service.enroll_student(course_id, student_id)

@router.get("/view-enrolled-courses")
async def view_enrolled_courses(student_id : str):
    return enrollment_service.view_enrolled_courses(student_id)

@router.patch("/assign-grade")
async def assign_grade(request : AssignGradeSchema):
    return enrollment_service.assign_grade(request)
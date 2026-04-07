from typing import List

from models.course import Course
from models.enums import UserRole
from models.user import User
from schemas.course_schema import CourseCreate
from schemas.user_schema import UserCreate

students: List[User] = []
facilitators: List[User] = []
courses: List[Course] = []

async def create_student(student: UserCreate)->User:
    if student.role != UserRole.STUDENT:
        raise Exception("Invalid role not allowed")
    new_id = len(students)+1
    new_student =  User(id=new_id,
                             name=student.name,
                             email=student.email,
                             role=student.role
                             )
    students.append(new_student)
    return new_student

async def create_facilitator(facilitator: UserCreate)->User:
    if facilitator.role != UserRole.FACILITATOR:
        raise Exception("Invalid role not allowed")
    new_id = len(facilitators)+1
    new_facilitator = await User(id=new_id,
                                 name=facilitator.name,
                                 email=facilitator.email,
                                 role=facilitator.role
                                 )
    facilitators.append(new_facilitator)
    return new_facilitator

async def get_students() -> List[User]:
    return students

async def get_facilitators() -> List[User]:
    return facilitators

async def create_course(course: CourseCreate)->Course:
    new_id = len(courses)+1
    new_course = Course(id=new_id,
                        title= course.title,
                        description= course.description,
                        facilitator_name= course.facilitator_name
                        )
    courses.append(new_course)
    return new_course
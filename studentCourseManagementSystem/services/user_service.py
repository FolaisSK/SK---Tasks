from typing import List

from database.connection import facilitator_collection, student_collection, course_collection
from exceptions.custom_exceptions import UserNotFoundException, UserAlreadyExistsException, InvalidRoleException, \
    CourseAlreadyExistsException, EmailAlreadyExistsException
from models.course import Course
from models.enums import UserRole
from models.user import User
from schemas.course_schema import CourseCreate
from schemas.user_schema import UserCreate
from repositories.user_repository import save, get_all_students, get_all_facilitators, get_facilitator_by_id, \
    get_student_by_id
from repositories.course_repository import save_course
from utils.sterilizers import map_user, map_course

students: List[User] = []
facilitators: List[User] = []
courses: List[Course] = []

def create_student(student: UserCreate)->User:
    existing_student =  student_collection.find_one({"email": student.email})
    if existing_student:
        raise EmailAlreadyExistsException()

    if student.role != UserRole.STUDENT:
        raise InvalidRoleException()
    new_id = len(students)+1
    new_student =  User(id=new_id,
                             name=student.name,
                             email=student.email,
                             role=student.role
                             )
    students.append(new_student)
    save(user= map_user(new_student))
    return new_student

def create_facilitator(facilitator: UserCreate)->User:
    existing_user =  facilitator_collection.find_one({"email": facilitator.email})
    if existing_user:
        raise EmailAlreadyExistsException()

    if facilitator.role != UserRole.FACILITATOR:
        raise InvalidRoleException()
    new_id = len(facilitators)+1
    new_facilitator =  User(id=new_id,
                                 name=facilitator.name,
                                 email=facilitator.email,
                                 role=facilitator.role
                                 )

    facilitators.append(new_facilitator)
    save(user= map_user(new_facilitator))
    return new_facilitator

def get_students() -> List[User]:
    return get_all_students()

def get_facilitators() -> List[User]:
    return get_all_facilitators()

def create_course(course: CourseCreate)->Course:
    existing_course =  course_collection.find_one({"title": course.title})
    if existing_course:
        raise CourseAlreadyExistsException()

    new_id = len(courses)+1
    new_course = Course(id=new_id,
                        title= course.title,
                        description= course.description,
                        facilitator_id= course.facilitator_id
                        )
    courses.append(new_course)
    save_course(course= map_course(new_course))
    return new_course


def find_facilitator(user_id):
    facilitator = get_facilitator_by_id(user_id)
    if facilitator is None:
        raise UserNotFoundException()
    return facilitator

def find_student(user_id):
    student = get_student_by_id(user_id)
    if student is None:
        raise UserNotFoundException()
    return student

from typing import List

from models.course import Course
from models.enrollment import Enrollment
from repositories.course_repository import get_course_by_id
from repositories.enrollment_repository import save_enrollment, get_enrollment_by_student_id_and_course_id, \
    update_grade, get_enrollments_by_student_id
from repositories.user_repository import get_student_by_id, get_facilitator_by_id
from schemas.enrollment_schema import AssignGradeSchema
from utils.sterilizers import map_enrollment

enrollments : List[Enrollment] = []

def enroll_student(course_id: str, student_id: str):
    course = get_course_by_id(course_id)
    student = get_student_by_id(student_id)
    if student is None:
        raise Exception('Student not found')
    if course is None:
        raise Exception('Course not found')

    new_id = len(enrollments)+1
    new_enrollment = Enrollment(id=new_id,
                                course_id=course_id,
                                student_id=student_id,
                                grade=None
                                )
    enrollments.append(new_enrollment)
    save_enrollment(enrollment=map_enrollment(new_enrollment))
    return new_enrollment

def assign_grade(request: AssignGradeSchema):
    facilitator = get_facilitator_by_id(request.facilitator_id)
    course = get_course_by_id(request.course_id)
    student = get_student_by_id(request.student_id)
    if student is None:
        raise Exception('Student not found')
    if course is None:
        raise Exception('Course not found')
    if facilitator is None:
        raise Exception('Facilitator not found')

    enrollment = get_enrollment_by_student_id_and_course_id(student_id=request.student_id, course_id=request.course_id)
    if enrollment is None:
        raise Exception('Enrollment not found')

    return update_grade(enrollment_id=enrollment["id"], grade=request.grade.upper())

def view_enrolled_courses(student_id : str) -> List[Enrollment]:
    student = get_student_by_id(student_id)
    if student is None:
        raise Exception('Student not found')
    return get_enrollments_by_student_id(student_id=student_id)
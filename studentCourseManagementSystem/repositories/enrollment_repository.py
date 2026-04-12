import pymongo
from bson import ObjectId

from database.connection import enrollment_collection
from exceptions.custom_exceptions import EnrollmentNotFoundException
from models.enrollment import Enrollment
from models.enums import Grades


def save_enrollment(enrollment: Enrollment):
    enrollment_collection.insert_one(enrollment)

def get_enrollment_by_id(enrollment_id):
    enrollment = enrollment_collection.find_one({'_id': ObjectId(enrollment_id)})
    del enrollment["_id"]
    if enrollment is not None:
        return enrollment
    return None

def get_enrollment_by_student_id_and_course_id(student_id: str, course_id: str):
    enrollment = enrollment_collection.find_one({'student_id': student_id, 'course_id': course_id})
    if enrollment is None:
        raise EnrollmentNotFoundException()
    enrollment["id"] = str(enrollment["_id"])
    del enrollment["_id"]
    if enrollment is not None:
        return enrollment
    return None

def get_all_enrollments():
    enrollments = list(enrollment_collection.find({}))
    for enrollment in enrollments:
        del enrollment["_id"]
    return enrollments

def update_grade(enrollment_id : str, grade : Grades):
    enrollment_collection.update_one({'_id': ObjectId(enrollment_id)}, {'$set': {'grade': grade}})
    return get_enrollment_by_id(enrollment_id)

def get_enrollments_by_student_id(student_id : str):
    enrollments = list(enrollment_collection.find({'student_id': student_id}))
    for enrollment in enrollments:
        del enrollment["_id"]
    return enrollments
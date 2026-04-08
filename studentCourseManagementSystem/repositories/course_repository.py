import pymongo
from bson import ObjectId

from database.connection import course_collection
from models.course import Course


def save_course(course: Course):
    course_collection.insert_one(course)


def get_course_by_id(course_id: str):
    course = course_collection.find_one({'_id': ObjectId(course_id)})
    del course["_id"]
    if course is not None:
        return course
    return None

def get_all_courses():
    courses = course_collection.find({})
    for course in courses:
        del course["_id"]
    return courses
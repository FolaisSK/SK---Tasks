import motor.motor_asyncio
import pymongo
from bson import ObjectId

from database.connection import student_collection, facilitator_collection
from exceptions.custom_exceptions import UserNotFoundException
from models.enums import UserRole
from models.user import User


def save(user: User):
    if user['role'] == UserRole.FACILITATOR:
        facilitator_collection.insert_one(user)
    else:
        student_collection.insert_one(user)

def get_facilitator_by_id(user_id: str):
    facilitator = facilitator_collection.find_one({'_id': ObjectId(user_id)})
    del facilitator["_id"]
    if facilitator is not None:
        return facilitator
    return None

def get_student_by_id(user_id: str):
    student = student_collection.find_one({'_id': ObjectId(user_id)})
    if student is None:
        raise UserNotFoundException()
    del student["_id"]
    if student is not None:
        return student
    return None

def get_all_facilitators():
    facilitators = list(facilitator_collection.find({}))

    for facilitator in facilitators:
        del facilitator["_id"]

    return facilitators

def get_all_students():
    students = list(student_collection.find({}))
    for student in students:
        del student["_id"]
    return students


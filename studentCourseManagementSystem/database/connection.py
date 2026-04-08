from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["student_course_management"]

student_collection = db["students"]
facilitator_collection = db["facilitators"]
course_collection = db["courses"]
enrollment_collection = db["enrollments"]
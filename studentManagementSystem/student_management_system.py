from studentManagementSystem.course import Course
from studentManagementSystem.student import Student


class StudentManagementSystem:
    def __init__(self):
        self.__students = {}
        self.__courses = {}

    def add_student(self, student: Student):
        self.__students[student.get_student_id()] = student

    def add_course(self, course: Course):
        self.__courses[course.get_course_code()] = course

    def get_students(self):
        return list(self.__students.keys())

    def get_courses(self, course_code):
        return list(self.__courses.keys())
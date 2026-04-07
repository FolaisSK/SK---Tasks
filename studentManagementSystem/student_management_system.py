from studentManagementSystem.course import Course
from studentManagementSystem.student import Student


class StudentManagementSystem:
    def __init__(self):
        self.__students = {}
        self.__courses = {}
        self.__student_count = 0

    def create_student(self, student_name, student_id):
        self.__students[self.generate_student_id()] = Student(student_name, self.generate_student_id())

    def generate_student_id(self):
        self.__student_count += 1
        id = "00" + str(self.__student_count)
        return id

    def add_student(self, student: Student):
        self.__students[student.get_student_id()] = student

    def add_course(self, course: Course):
        self.__courses[course.get_course_code()] = course

    def get_students(self):
        return list(self.__students.keys())

    def get_courses(self, course_code):
        return list(self.__courses.keys())
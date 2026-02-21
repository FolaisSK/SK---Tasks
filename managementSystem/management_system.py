from managementSystem.course import Course
from managementSystem.student import Student


class ManagementSystem:
    def __init__(self):
        self.__students = {}
        self.__courses = {}
        self.student_counter = 0

    def create_student(self, student_name, student_age):
        student = Student(student_name, student_age, self.generate_matric_number())
        self.__students[student.get_matric_number()] = student
        return student

    def generate_matric_number(self):
        self.student_counter += 1
        return "00" + str(self.student_counter)

    def get_student_matric_number(self, student_name):
        return Student.get_matric_number(student_name)

    def update_student(self, matric_number, new_student_name):
        student = self.__find_student_by_id(matric_number)
        student.set_name(new_student_name)

    def __find_student_by_id(self, matric_number):
        for student in self.__students:
            if student == matric_number:
                return self.__students[student]
        return None

    def create_course(self, course_code, course_title, credit_unit):
        course = Course(course_code, course_title, credit_unit)
        self.__courses[course_code] = course
        return course

    def get_courses(self):
        return self.__courses

    def enroll_student(self, matric_number, course_code):
        student = self.__find_student_by_id(matric_number)
        course = self.__find_course_by_course_code(course_code)
        student.register_course(course_code, course)

    def __find_course_by_course_code(self, course_code):
        for course in self.__courses:
            if course == course_code:
                return self.__courses[course_code]
        raise Exception("Course not found")

    def grade_student(self, matric_number, course_code, course_grade):
        self.__validate_grade(course_grade)
        student = self.__find_student_by_id(matric_number)
        student.grade_course(course_code,course_grade)

    def get_student_grade(self, matric_number, course_code):
        student = self.__find_student_by_id(matric_number)
        return student.get_grade(course_code)

    def __validate_grade(self, grade):
        if grade < 0 or grade > 100:
            raise Exception("Grade must be between 0 and 100")
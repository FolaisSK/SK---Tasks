from studentManagementSystem.course import Course


def validate_grade(grade: int):
    if not 0 <= grade <= 100:
        raise ValueError('Invalid grade')

def validate_course(course: Course):
    if not course.get_course_code():
        raise ValueError('Invalid course')

def validated_offered_course(course: Course, courses):
    if course.get_course_code()  in courses:
        raise ValueError('Course already enrolled')


class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__courses_grades = {}

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def update_name(self, name):
        if not name:
            raise ValueError('Invalid name')
        self.__name = name

    def enroll_student(self, course: Course):
        validated_offered_course(course, self.get_courses())
        validate_course(course)
        self.__courses_grades[course.get_course_code()] = None

    def grade_student(self, course: Course, grade: int):
        validate_course(course)
        validate_grade(grade)
        self.__courses_grades[course.get_course_code()] = grade

    def get_grade(self, course: Course):
        validate_course(course)
        return self.__courses_grades.get(course.get_course_code())

    def get_courses(self):
        return list(self.__courses_grades.keys())
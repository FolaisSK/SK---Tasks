from managementSystem.course import Course


class Student:
    def __init__(self, name, age, matric_number):
        self.validate_age(age)
        self.__name = name
        self.__age = age
        self.__matric_number = matric_number
        self.__enrolled_courses = {}
        self.__course_grades = {}

    def get_matric_number(self):
        return self.__matric_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def register_course(self,course_code, course: Course):
        self.__enrolled_courses[course_code] = course
        self.__course_grades[course_code] = 0

    def offered_courses(self):
        return self.__enrolled_courses

    def grade_course(self, course_code, course_grade):
        self.__course_grades[course_code] = course_grade

    def get_grade(self, course_code):
       for course in self.__course_grades:
           if course == course_code:
               print(self.__course_grades[course_code])
               return self.__course_grades[course_code]
       return None

    def validate_age(self, age):
        if age < 16 or age > 40:
            raise Exception('Age must be between 16 and 40')
import re


class Course:
    def __init__(self, course_name, course_code, credit_unit):
        self.validate_course_name(course_name)
        self.__course_name = course_name
        self.__course_code = course_code
        self.__credit_unit = credit_unit

    def validate_course_name(self, course_name):
        name = 'Valid' if re.match(r'[A-Z]{3}\d{3}$', course_name) else 'Invalid'
        if name == 'Invalid':
            raise Exception('Invalid course name')


class Course:
    def __init__(self, course_name, course_code, credit_unit):
        self.__course_name = course_name
        self.__course_code = course_code
        self.__credit_unit = credit_unit

    def get_course_name(self):
        return self.__course_name

    def get_course_code(self):
        return self.__course_code

    def get_credit_unit(self):
        return self.__credit_unit
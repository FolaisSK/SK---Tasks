import unittest

from managementSystem.course import Course
from managementSystem.management_system import ManagementSystem


class MyStudentManagementSystem(unittest.TestCase):
    def setUp(self):
        self.university = ManagementSystem()

    def test_student_can_be_created(self):
        self.student = self.university.create_student("Fola", 23)
        self.assertEqual("001", self.student.get_matric_number())

    def test_student_cannot_be_created_with_age_less_than_16_greater_than_40(self):
        with self.assertRaises(Exception):
            self.student = self.university.create_student("Bimbo", 12)
        with self.assertRaises(Exception):
            self.student = self.university.create_student("Fola", 55)

    def test_that_student_name_can_be_updated_via_university(self):
        self.student = self.university.create_student("Fola", 23)
        self.assertEqual("001", self.student.get_matric_number())
        self.university.update_student("001", "Folajimi")
        self.assertEqual("Folajimi", self.student.get_name())

    def test_student_cannot_be_updated_with_wrong_matic_number(self):
        self.student = self.university.create_student("Fola", 23)
        self.assertEqual("001", self.student.get_matric_number())
        with self.assertRaises(Exception):
            self.university.update_student("002", "Folajimi")

    def test_that_course_can_be_created(self):
        self.course = self.university.create_course("ICE517", "Queuing Theory", 3)
        self.assertIn("ICE517", self.university.get_courses())

    def test_that_course_cant_be_created_with_invalid_course_code(self):
        with self.assertRaises(Exception):
            self.university.create_course("Food1010", "Queuing Theory", 3)

    def test_student_can_be_enrolled_in_a_course(self):
        self.student = self.university.create_student("Folajimi", 23)
        self.assertEqual("001", self.student.get_matric_number())
        self.course = self.university.create_course("ICE517", "Queuing Theory", 3)
        self.university.enroll_student("001", "ICE517")
        self.assertIn("ICE517", self.student.offered_courses())

    def test_student_cant_be_enrolled_in_a_course_that_does_not_exist(self):
        self.student = self.university.create_student("Fola", 23)
        self.assertEqual("001", self.student.get_matric_number())
        with self.assertRaises(Exception):
            self.university.enroll_student("001", "GEC510")

    def test_that_student_can_be_graded_in_a_course(self):
        self.student = self.university.create_student("Fola", 23)
        self.assertEqual("001", self.student.get_matric_number())
        self.course = self.university.create_course("ICE517", "Queuing Theory", 3)
        self.university.enroll_student("001", "ICE517")
        self.assertIn("ICE517", self.student.offered_courses())
        self.university.grade_student("001", "ICE517", 80)
        grade = self.university.get_student_grade("001", "ICE517")
        self.assertEqual(80, grade)

    def test_that_student_cant_have_invalid_graded_in_a_course(self):
        self.student = self.university.create_student("Fola", 23)
        self.assertEqual("001", self.student.get_matric_number())
        self.course = self.university.create_course("ICE517", "Queuing Theory", 3)
        self.university.enroll_student("001", "ICE517")
        self.assertIn("ICE517", self.student.offered_courses())
        with self.assertRaises(Exception):
            self.university.grade_student("001", "ICE517", -20)
        with self.assertRaises(Exception):
            self.university.grade_student("001", "ICE517", 120)

if __name__ == '__main__':
    unittest.main()

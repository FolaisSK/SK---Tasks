import unittest

from studentManagementSystem.course import Course
from studentManagementSystem.student import Student
from studentManagementSystem.student_management_system import StudentManagementSystem


class MyStudentManagementSystem(unittest.TestCase):
    def setUp(self):
        self.student = Student("Fola", "456")
        self.course1 = Course("Queuing Theory", "ICE501", 3)
        self.university = StudentManagementSystem()

    def test_student_creation(self):
        self.assertEqual(self.student.get_name(), "Fola")
        self.assertEqual(self.student.get_student_id(), "456")

    def test_course_creation(self):
        self.assertEqual(self.course1.get_course_name(), "Queuing Theory")
        self.assertEqual(self.course1.get_course_code(), "ICE501")

    def test_student_name_update(self):
        self.assertEqual(self.student.get_name(), "Fola")
        self.student.update_name("Folajimi Lawal")
        self.assertEqual(self.student.get_name(), "Folajimi Lawal")

    def test_student_can_be_enrolled_in_a_course(self):
        self.assertEqual(self.student.get_student_id(), "456")
        self.student.enroll_student(self.course1)
        self.assertIn(self.course1.get_course_code(),self.student.get_courses())

    def test_student_can_be_graded_in_enrolled_course(self):
        self.assertEqual(self.student.get_student_id(), "456")
        self.student.enroll_student(self.course1)
        self.assertIn(self.course1.get_course_code(),self.student.get_courses())
        self.student.grade_student(self.course1, 70)
        self.assertEqual(self.student.get_grade(self.course1), 70)

    def test_invalid_grade(self):
        self.assertEqual(self.student.get_student_id(), "456")
        self.student.enroll_student(self.course1)
        self.assertIn(self.course1.get_course_code(), self.student.get_courses())
        with self.assertRaises(ValueError):
            self.student.grade_student(self.course1, 120)

    def test_invalid_course(self):
        self.assertEqual(self.student.get_student_id(), "456")
        self.student.enroll_student(self.course1)
        with self.assertRaises(AssertionError):
            self.assertIn("comp101", self.student.get_courses())

    def test_duplicate_enrollment_raises_error(self):
        self.assertEqual(self.student.get_student_id(), "456")
        self.student.enroll_student(self.course1)
        self.assertIn(self.course1.get_course_code(), self.student.get_courses())
        with self.assertRaises(ValueError):
            self.student.enroll_student(self.course1)

    def test_add_student_to_university_system(self):
        self.assertEqual(self.student.get_student_id(), "456")
        self.student.enroll_student(self.course1)
        self.assertIn(self.course1.get_course_code(), self.student.get_courses())
        self.university.add_student(self.student)
        self.assertIn(self.student.get_student_id(), self.university.get_students())

if __name__ == '__main__':
    unittest.main()

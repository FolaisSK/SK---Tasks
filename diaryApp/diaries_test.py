import unittest

from diaryApp.diaries import Diaries


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.diaries = Diaries()

    def test_that_diary_can_be_added_to_list_of_diaries(self):
        self.diaries.add("folaissk", "123abc")
        diary = self.diaries.find_by_username("folaissk")
        self.assertEqual("folaissk", diary.get_username())

    def test_that_diary_can_be_deleted_from_diaries(self):
        self.diaries.add("folaissk", "123abc")
        diary = self.diaries.find_by_username("folaissk")
        self.assertEqual("folaissk", diary.get_username())
        self.diaries.delete("folaissk", "123abc")
        with self.assertRaises(Exception):
            self.diaries.find_by_username("folaissk")


if __name__ == '__main__':
    unittest.main()

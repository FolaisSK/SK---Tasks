import unittest

from diaryApp.diary import Diary


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("folaissk", "abc123")
        self.diary_two = None

    def test_that_diary_can_be_unlocked(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("abc123")
        self.assertFalse(self.diary.is_locked())

    def test_that_diary_can_be_locked_after_being_unlocked(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("abc123")
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_cannot_be_created_with_password_less_than_four_characters(self):
        with self.assertRaises(Exception):
            self.diary_two = Diary("folajimi", "ab1")

    def test_that_diary_cannot_be_unlocked_with_wrong_password(self):
        self.assertTrue(self.diary.is_locked())
        with self.assertRaises(Exception):
            self.diary.unlock_diary("23def")

    def test_that_an_entry_can_be_created(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("abc123")
        self.assertFalse(self.diary.is_locked())
        self.diary.create_entry(
            "The Flash",
            "A story about a man who was struck by lightning, and became the fastest man alive"
        )
        entry = self.diary.find_entry_by_id(1)
        self.assertEqual("The Flash", entry.get_title())

    def test_that_while_diary_is_locked_an_entry_cant_be_created(self):
        self.assertTrue(self.diary.is_locked())
        with self.assertRaises(Exception):
            self.diary.create_entry(
                "The Flash",
                "A story about a man who was struck by lightning, and became the fastest man alive"
            )

    def test_that_an_entry_created_can_be_deleted(self):
        self.diary.unlock_diary("abc123")
        self.diary.create_entry(
            "The Flash",
            "A story about a man who was struck by lightning, and became the fastest man alive"
        )
        entry = self.diary.find_entry_by_id(1)
        self.assertEqual("The Flash", entry.get_title())
        self.diary.delete_entry(1)
        with self.assertRaises(Exception):
            self.diary.find_entry_by_id(1)

    def test_that_while_diary_is_locked_an_entry_cant_be_deleted(self):
        self.diary.unlock_diary("abc123")
        self.diary.create_entry(
            "The Flash",
            "A story about a man who was struck by lightning, and became the fastest man alive"
        )
        self.diary.lock_diary()
        with self.assertRaises(Exception):
            self.diary.delete_entry(1)

    def test_that_an_entry_can_be_updated(self):
        self.diary.unlock_diary("abc123")
        self.diary.create_entry(
            "The Flash",
            "A story about a man who was struck by lightning, and became the fastest man alive"
        )
        entry = self.diary.find_entry_by_id(1)
        self.assertEqual("The Flash", entry.get_title())
        self.diary.update_entry(
            1,
            "Martin Luther King",
            "Patriotism at it's finest, racism at it's worst"
        )
        self.assertEqual("Martin Luther King", entry.get_title())

    def test_that_while_diary_is_locked_an_entry_cant_be_updated(self):
        self.diary.unlock_diary("abc123")
        self.diary.create_entry(
            "The Flash",
            "A story about a man who was struck by lightning, and became the fastest man alive"
        )
        self.diary.lock_diary()
        with self.assertRaises(Exception):
            self.diary.update_entry(
                1,
                "Martin Luther King",
                "Patriotism at it's finest, racism at it's worst"
            )

    def test_that_while_diary_is_locked_throws_exception_if_locked_again(self):
        self.assertTrue(self.diary.is_locked())
        with self.assertRaises(Exception):
            self.diary.lock_diary()

    def test_that_while_diary_is_unlocked_throws_exception_if_unlocked_again(self):
        self.diary.unlock_diary("abc123")
        with self.assertRaises(Exception):
            self.diary.unlock_diary("abc123")


if __name__ == '__main__':
    unittest.main()

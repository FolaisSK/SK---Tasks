import unittest

from televisionSystem.television import Television


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tv = Television()

    def test_that_tv_can_be_turned_on(self):
        self.assertFalse(self.tv.is_on())
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on())

    def test_that_tv_can_be_turned_off(self):
        self.assertFalse(self.tv.is_on())
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on())
        self.tv.turn_off()
        self.assertFalse(self.tv.is_on())

    def test_volume_is_30_when_turned_on(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on())
        self.assertEqual(self.tv.get_volume(), 30)

    def test_volume_increases_when_on(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on())
        self.assertEqual(self.tv.get_volume(), 30)
        self.tv.increase_volume()
        self.assertEqual(self.tv.get_volume(), 31)

    def test_volume_does_not_exceed_max_volume(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on())
        for volume in range(75):
            self.tv.increase_volume()
        self.assertEqual(self.tv.get_volume(), 100)

    def test_volume_decreases_when_on(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on())
        self.assertEqual(self.tv.get_volume(), 30)
        self.tv.decrease_volume()
        self.assertEqual(self.tv.get_volume(), 29)

    def test_volume_can_be_muted_when_on(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on())
        self.assertEqual(self.tv.get_volume(), 30)
        for volume in range(30):
            self.tv.decrease_volume()
        self.assertEqual(self.tv.get_volume(), 0)

    def test_volume_does_not_go_below_min_volume(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on())
        for volume in range(40):
            self.tv.decrease_volume()
        self.assertEqual(self.tv.get_volume(), 0)

    def test_valid_channel_change(self):
        self.tv.turn_on()
        self.tv.set_channel(50)
        self.assertEqual(self.tv.get_channel(), 50)

    def test_invalid_channel_raises_error(self):
        self.tv.turn_on()
        with self.assertRaises(ValueError):
            self.tv.set_channel(101)

    def test_cannot_change_volume_when_off(self):
        with self.assertRaises(Exception):
            self.tv.increase_volume()

    def test_cannot_change_channel_when_off(self):
        with self.assertRaises(Exception):
            self.tv.set_channel(10)

if __name__ == '__main__':
    unittest.main()

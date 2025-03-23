import unittest
from datetime import date

from date_time import calculate_age


class TestCalculateAge(unittest.TestCase):
    def test_birthday_today(self):
        birth_date = date(2000, 3, 22)  # Same as today's date
        self.assertEqual(calculate_age(birth_date), 25)

    def test_birthday_passed_this_year(self):
        birth_date = date(2000, 1, 1)  # Birthday already passed this year
        self.assertEqual(calculate_age(birth_date), 25)

    def test_birthday_not_yet_this_year(self):
        birth_date = date(2000, 12, 31)  # Birthday not yet this year
        self.assertEqual(calculate_age(birth_date), 24)

    def test_leap_year_birthday(self):
        birth_date = date(2000, 2, 29)  # Leap year birthday
        self.assertEqual(calculate_age(birth_date), 25)


if __name__ == "__main__":
    unittest.main()

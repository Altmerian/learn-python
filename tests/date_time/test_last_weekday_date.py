import unittest
from datetime import datetime, timedelta, date

from date_time import get_last_weekday_date


class TestLastWeekdayDate(unittest.TestCase):
    def test_integer_input(self):
        """Test with integer inputs (0-6)"""
        for i in range(7):
            result = get_last_weekday_date(i)
            self.assertIsInstance(result, date)
            # Verify the returned date is the correct day of week
            self.assertEqual(result.weekday(), i)
            # Verify the date is not in the future
            self.assertLessEqual(result, datetime.now().date())
            # Verify the date is within the last 7 days
            self.assertGreaterEqual(result, datetime.now().date() - timedelta(days=7))

    def test_full_day_name(self):
        """Test with full day names"""
        day_names = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        for i, name in enumerate(day_names):
            result = get_last_weekday_date(name)
            self.assertEqual(result.weekday(), i)

    def test_abbreviated_day_name(self):
        """Test with abbreviated day names"""
        day_abbrs = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, abbr in enumerate(day_abbrs):
            result = get_last_weekday_date(abbr)
            self.assertEqual(result.weekday(), i)

    def test_digit_string_input(self):
        """Test with string digits ('0'-'6')"""
        for i in range(7):
            str_i = str(i)
            result = get_last_weekday_date(str_i)
            self.assertEqual(result.weekday(), i)

    def test_case_insensitivity(self):
        """Test case insensitivity for day names"""
        variants = [
            ("monday", 0),
            ("MONDAY", 0),
            ("Monday", 0),
            ("MON", 0),
            ("Mon", 0),
            ("mon", 0),
        ]
        for day_str, expected_weekday in variants:
            result = get_last_weekday_date(day_str)
            self.assertEqual(result.weekday(), expected_weekday)

    def test_invalid_string_input(self):
        """Test invalid string inputs"""
        invalid_inputs = ["Not a day", "Monnday", "M0nday", "7", "8", "-1"]
        for invalid in invalid_inputs:
            with self.assertRaises(ValueError):
                get_last_weekday_date(invalid)

    def test_out_of_range_integer(self):
        """Test out of range integer inputs"""
        invalid_ints = [-1, 7, 8, 100]
        for invalid in invalid_ints:
            with self.assertRaises(ValueError):
                get_last_weekday_date(invalid)

    def test_most_recent_date(self):
        """Test that the returned date is the most recent occurrence of that weekday"""
        today = datetime.now().date()
        today_weekday = today.weekday()

        for day in range(7):
            result = get_last_weekday_date(day)

            # If the day is today, the result should be today
            if day == today_weekday:
                self.assertEqual(result, today)
            # If the day is earlier in the week than today, the result should be days_diff days ago
            elif day < today_weekday:
                days_diff = today_weekday - day
                self.assertEqual(result, today - timedelta(days=days_diff))
            # If the day is later in the week than today, the result should be from last week
            else:
                days_diff = today_weekday + 7 - day
                self.assertEqual(result, today - timedelta(days=days_diff))


if __name__ == "__main__":
    unittest.main()

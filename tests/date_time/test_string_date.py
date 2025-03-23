import unittest
from datetime import date

from date_time import parse_date


class TestParseDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(parse_date("01-01-2023"), date(2023, 1, 1))

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            parse_date("2023-01-01")

    def test_missing_parts(self):
        with self.assertRaises(ValueError):
            parse_date("01-2023")

    def test_non_numeric_parts(self):
        with self.assertRaises(ValueError):
            parse_date("01-XX-2023")

    def test_invalid_day(self):
        with self.assertRaises(ValueError):
            parse_date("32-01-2023")

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            parse_date("01-13-2023")


if __name__ == "__main__":
    unittest.main()

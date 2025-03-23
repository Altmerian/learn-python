import unittest

from date_time import day_of_year


class TestDayOfYear(unittest.TestCase):
    def test_valid_dates(self):
        # Test regular dates
        self.assertEqual(day_of_year("01/01/2025"), 1)
        self.assertEqual(day_of_year("31/12/2025"), 365)

        # Test leap year date
        self.assertEqual(day_of_year("29/02/2024"), 60)  # 2024 is a leap year

    def test_invalid_formats(self):
        # Test invalid date formats
        with self.assertRaises(ValueError):
            day_of_year("2025/01/01")  # Wrong format YYYY/MM/DD

        with self.assertRaises(ValueError):
            day_of_year("01-01-2025")  # Wrong separator

        with self.assertRaises(ValueError):
            day_of_year("1/1/2025")  # Missing leading zeros

        with self.assertRaises(ValueError):
            day_of_year("invalid")  # Complete nonsense

    def test_invalid_dates(self):
        # Test invalid dates
        with self.assertRaises(ValueError):
            day_of_year("32/01/2025")  # Invalid day

        with self.assertRaises(ValueError):
            day_of_year("29/02/2025")  # Not a leap year

        with self.assertRaises(ValueError):
            day_of_year("31/04/2025")  # Invalid day for April


if __name__ == "__main__":
    unittest.main()

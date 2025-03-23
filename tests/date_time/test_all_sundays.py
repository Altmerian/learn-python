import unittest

from date_time import all_sundays


class TestAllSundays(unittest.TestCase):
    def test_non_leap_year(self):
        """Test the function with a non-leap year (2023)"""
        self.assertEqual(all_sundays(2023), 53)  # 2023 has 53 Sundays

    def test_leap_year(self):
        """Test the function with a leap year (2024)"""
        self.assertEqual(all_sundays(2024), 52)

    def test_leap_year_53_sundays(self):
        """Test a leap year with 53 Sundays (2012)"""
        self.assertEqual(all_sundays(2012), 53)

    def test_non_leap_year_53_sundays(self):
        """Test a non-leap year with 53 Sundays (2017)"""
        self.assertEqual(all_sundays(2017), 53)

    def test_current_year(self):
        """Test the function with the current year (2025)"""
        self.assertEqual(all_sundays(2025), 52)

    def test_known_years(self):
        """Test with known results for various years"""
        test_data = {
            2000: 53,  # Year starts on Saturday, has 366 days (leap year)
            2001: 52,  # Year starts on Monday, has 365 days
            2002: 52,  # Year starts on Tuesday, has 365 days
            2003: 52,  # Year starts on Wednesday, has 365 days
            2004: 52,  # Year starts on Thursday, has 366 days (leap year)
            2005: 52,  # Year starts on Saturday, has 365 days
            2006: 53,  # Year starts on Sunday, has 365 days
            2028: 53,  # Year starts on Saturday, has 366 days (leap year)
        }

        for year, expected in test_data.items():
            with self.subTest(year=year):
                self.assertEqual(all_sundays(year), expected)


if __name__ == "__main__":
    unittest.main()

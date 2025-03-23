import unittest
import calendar

from date_time import second_saturday_dates


class TestSecondSaturdayDates(unittest.TestCase):
    def test_year_2025(self):
        """Test second Saturdays for all months in 2025"""
        result = second_saturday_dates(2025)

        # Verify return type
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 12)  # Should have all 12 months

        # Known second Saturdays for 2025
        expected = {
            "January": 11,
            "February": 8,
            "March": 8,
            "April": 12,
            "May": 10,
            "June": 14,
            "July": 12,
            "August": 9,
            "September": 13,
            "October": 11,
            "November": 8,
            "December": 13,
        }

        self.assertEqual(result, expected)

    def test_leap_year(self):
        """Test second Saturdays in a leap year (2024)"""
        result = second_saturday_dates(2024)

        # Test a few known dates in leap year
        self.assertEqual(result["January"], 13)
        self.assertEqual(result["February"], 10)  # Affected by leap year
        self.assertEqual(result["March"], 9)

    def test_month_names(self):
        """Test that month names are correctly used as keys"""
        result = second_saturday_dates(2025)
        expected_months = list(calendar.month_name)[
            1:
        ]  # month_name starts with empty string

        self.assertEqual(sorted(result.keys()), sorted(expected_months))

    def test_date_ranges(self):
        """Test that all dates are within valid ranges"""
        result = second_saturday_dates(2025)

        for month in result:
            date = result[month]
            self.assertIsInstance(date, int)
            self.assertGreaterEqual(date, 8)  # Second Saturday can't be before the 8th
            self.assertLessEqual(date, 14)  # Second Saturday can't be after the 14th

    def test_day_is_saturday(self):
        """Test that each date actually falls on a Saturday"""
        year = 2025
        result = second_saturday_dates(year)

        for month_name, day in result.items():
            month_num = list(calendar.month_name).index(month_name)
            weekday = calendar.weekday(year, month_num, day)
            self.assertEqual(weekday, calendar.SATURDAY)

    def test_is_second_saturday(self):
        """Test that each date is actually the second Saturday"""
        year = 2025
        result = second_saturday_dates(year)

        for month_name, day in result.items():
            month_num = list(calendar.month_name).index(month_name)
            c = calendar.monthcalendar(year, month_num)
            saturdays = [
                week[calendar.SATURDAY] for week in c if week[calendar.SATURDAY] != 0
            ]
            self.assertEqual(day, saturdays[1])  # Should be the second Saturday


if __name__ == "__main__":
    unittest.main()

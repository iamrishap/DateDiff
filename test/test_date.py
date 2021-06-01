import unittest

from src.date import days_between, Date


class TestDate(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(Date._leap_year(1964), True)
        self.assertEqual(Date._leap_year(1600), True)  # Divisible by 400
        self.assertEqual(Date._leap_year(1900), False)  # Divisible by 100 but not by 400
        self.assertEqual(Date._leap_year(1901), False)

    def test_valid_date(self):
        self.assertEqual(Date._validate_date('02/07/1983'), (2, 7, 1983))
        self.assertEqual(Date._validate_date('29/02/1600'), (29, 2, 1600))
        self.assertEqual(Date._validate_date('28/02/1986'), (28, 2, 1986))
        self.assertRaises(ValueError, Date._validate_date, '32/01/1987')  # Incorrect date
        self.assertRaises(ValueError, Date._validate_date, '12/22/1987')  # Incorrect month
        self.assertRaises(ValueError, Date._validate_date, '29/02/1987')  # 29 days in Feb in non-leap year

    def test_days_between(self):
        self.assertEqual(days_between(Date('02/06/1983'), Date('22/06/1983')), 19)
        self.assertEqual(days_between(Date('04/07/1984'), Date('25/12/1984')), 173)
        self.assertEqual(days_between(Date('03/01/1989'), Date('03/08/1983')), 1979)

from typing import Tuple

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Date:
    def __init__(self, date_string: str):
        self.day, self.month, self.year = self._validate_date(date_string)

    def __str__(self):
        return f'Date(day={self.day}, month={self.month}, year={self.year})'

    @staticmethod
    def _leap_year(year: int) -> bool:
        """ Checks if an year is leap or not

        :param year: The year to check
        :return: True if leap year, False otherwise
        """
        return year % 100 != 0 and year % 4 == 0 or year % 400 == 0

    @staticmethod
    def _validate_date(date_string: str) -> Tuple[int, int, int]:
        """ Parses the date string and validates the values and returns the sanitised data

        :param date_string: DD/MM/YYYY format string representing the date
        :return: 3-tuple of (day, month, year) values
        """
        day, month, year = map(int, date_string.split('/'))
        if year < 0:
            raise ValueError("Year needs to be a non-negative value.")
        if month < 1 or month > 12:
            raise ValueError("Month needs to be between 1 and 12.")
        if (
                day < 0 or
                (day > 29 and month == 2) or
                (day == 29 and month == 2 and not Date._leap_year(year)) or
                (day > days_in_month[month-1] and month != 2)  # Feb got the special treatment already
        ):
            raise ValueError("Not a valid date for this month and year combination.")
        return day, month, year


def days_between(date_one: Date, date_two: Date) -> int:
    """ Finds the number of days between two Dates (non-inclusive difference)

    :param date_one: Date object one
    :param date_two: Date object two
    :return: number of days between date_one and date_two
    """
    def _leap_years_count(date: Date):
        years = date.year if date.month > 2 else date.year - 1
        return years // 4 - years // 100 + years // 400

    # Find the number of days from 00/00/0000 to date one
    date_one_days = date_one.year * 365 + date_one.day + _leap_years_count(date_one)
    for month in range(0, date_one.month - 1):
        date_one_days += days_in_month[month-1]

    # Find the number of days from 00/00/0000 to date two
    date_two_days = date_two.year * 365 + date_two.day + _leap_years_count(date_two)
    for month in range(0, date_two.month - 1):
        date_two_days += days_in_month[month-1]

    return abs(date_one_days - date_two_days) - 1  # Excluding the edges


def date_input():
    while True:
        try:
            date_one_string = input("Input the date string: ")
            return Date(date_one_string)
        except ValueError as VE:
            print(VE)
        if input("Want to try again? (y|n) ") in ['y', 'Y', 'yes', 'Yes', 'YES']:
            continue
        else:
            print("Exiting on user request.")
            exit(0)


if __name__ == "__main__":
    print("Utility to calculate the number of days between two dates (DD/MM/YYYY format)")
    print("\nFirst date")
    dt1 = date_input()
    print("\nSecond date")
    dt2 = date_input()
    print(f"\nDays between {dt1} and {dt2} = {days_between(dt1, dt2)}")

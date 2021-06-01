# DateDiff
A command line utility that finds the number of days between two passed dates without using any datetime library.

## Sample Run

- Run 1

```
First date
Input the date string: 03/01/1989

Second date
Input the date string: 03/08/1983

Days between Date(day=3, month=1, year=1989) and Date(day=3, month=8, year=1983) = 1979
```

- Run 2

```
First date
Input the date string: 29/02/1987
Not a valid date for this month and year combination.
Want to try again? (y|n) y
Input the date string: 23/13/2891
Month needs to be between 1 and 12.
Want to try again? (y|n) y
Input the date string: 03/10/1990

Second date
Input the date string: 01/06/2021

Days between Date(day=3, month=10, year=1990) and Date(day=1, month=6, year=2021) = 11197
```

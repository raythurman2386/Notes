# Identify Leap Years
"""
The year can be evenly divided by 4 is a leap year unless:
  The year can be evenly divided by 100, unless:
    The year is also divisible by 400
"""

# See if year can be divided by 4
# If not return false
# else check if the year can be divided by both
# 100 and 400


def leap_year(year):
    leap = False

    if year % 4 == 0:
        if year % 100 != 0:
            leap = True
        elif year % 100 == 0 and year % 400 == 0:
            leap = True
        else:
            leap = False
    return leap


print(leap_year(2000), '2000')
print(leap_year(2400), '2400')
print(leap_year(2200), '2200')
print(leap_year(2100), '2100')
print(leap_year(1900), '1900')
print(leap_year(1992), '1992')

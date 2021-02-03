"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import date, datetime, time

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent: int = int(input("Target percent vaccinated: "))

days: int = round(((target_percent / 100 * population - doses_administered / 2) / doses_per_day * 2))
today: datetime = datetime.today()
future: timedelta = timedelta(days)
date_vaccinated: datetime = today + future


print("We will reach " + str(target_percent) + "% vaccination in " + str(days) + ", which falls on " + date_vaccinated.strftime("%B %d, %Y"))
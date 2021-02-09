"""A vaccination calculator."""

__author__ = "730395239"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

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
target: int = int(input("Target percent vaccinated: "))

days: int = round(((target / 100 * population - doses_administered / 2) / doses_per_day * 2))
today: datetime = datetime.today()
future: timedelta = timedelta(days)
date_vaccinated: datetime = today + future
date: str = date_vaccinated.strftime("%B %d, %Y")

print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + date)
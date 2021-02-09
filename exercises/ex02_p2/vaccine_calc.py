"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    date: str = future_date(days)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + date + ".")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Returns number of days until target percentage is vaccinated."""
    return round(((target / 100 * population - doses / 2) / doses_per_day * 2))


# TODO 3: Define future_date function
def future_date(number_days: int) -> str:
    """Returns projected date goal will reach in Month DD, YYYY form."""
    today: datetime = datetime.today()
    future: timedelta = timedelta(number_days)
    date_vaccinated: datetime = today + future
    return date_vaccinated.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()

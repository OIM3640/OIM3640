import time


def did_you_mean_gorundhog_day():
    print("Did you mean: Goundhog Day?")
    time.sleep(1)
    did_you_mean_gorundhog_day()


# did_you_mean_gorundhog_day()


def did_you_mean(query):
    """
    Simulate Google's meme for recursion,
    aka. print Did you mean: <query>, then wait for 1 second and print again recursively

    (This is docstring for function, which a summary of this funciton.)
    """
    print(f"Did you mean: {query}?")
    time.sleep(1)
    did_you_mean(query)


def f():
    print("hi")


# did_you_mean("recursion")


def is_leap_year(year):
    """Check whether a year is a leap year."""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


is_leap_year(2024)
is_leap_year(2025)

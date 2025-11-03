print("A lot of tasks...")

# try:
#     number = int(input("Enter a number: "))
#     result = 2025 / number
#     print(result)
# except ZeroDivisionError:
#     print("You cannot enter 0.")
# except ValueError:
#     print("❗You have to enter an integer!")
# finally:
#     print("No matter what happens, we will get here.")


class SomeWeirdException(Exception):
    """"""


def process_data():
    data = ["tauria", "russel", "bertrand", 2025, "daniel"]

    for s in data:
        try:
            print(s[0])
        except TypeError:
            print(f"Skipping invalid entry: {s}")


def process_string(s):
    if not isinstance(s, str):
        raise SomeWeirdException("Not a string!")
    print(s.upper())


def main():
    try:
        process_data()
        process_string(1234)
    except SomeWeirdException:
        print("I met some weird error and I know how to handle it here.")
    print("Move on to the next task...")


main()

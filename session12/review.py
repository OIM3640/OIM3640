import math

def find_next_pefect_square(year):
    # how to check whether a number is a perfect square number?

    # print(int(math.sqrt(year)) **2 == year)

    # How to find the next perfect square number
    counter = 0
    while True:
        year += 1
        if int(math.sqrt(year)) **2 == year:
            print(f'Next perfect square year is {year}!')
            counter += 1
            if counter == 5:
                return

find_next_pefect_square(2025)
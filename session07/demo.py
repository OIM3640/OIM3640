# age = 3
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# elif age >= 0:
#     print('baby')
# else:
#     print('unborn')


# age = 20
# if age >= 6:
#     print("teenager")


# if age >= 18:
#     print("adult")
# else:
#     print("kid")


# Recursion

import time


def recur():
    print("Did you mean: recursion?")
    time.sleep(1)
    recur()


# recur()


def countdown(n):
    """"""
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        time.sleep(1)
        countdown(n - 1)


countdown(5)

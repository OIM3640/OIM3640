def sqrt(x):
    return x**0.5, -(x**0.5)


# result = sqrt(25)
# print(result)
# root_1, root_2 = sqrt(25)
# print(root_1, root_2)


# print(divmod(10, 3))


def f():
    print("Hi")
    return "hello"


# result = f()
# print(type(f))
# # print(result)
# print(type(result))


# score = 95

# if score >= 60:
#     print("Pass")
# if score >= 90:
#     print("A")
# else:
#     print("Fail")


def grade(score):
    if score >= 60:
        return "Pass"
    if score >= 90:
        return "A"
    elif score >= 0:
        return "Fail"

    return "Invalid score"


# result = grade(95)
# result = grade(-1)
# print(result)

# username = input("Username: ")
# password = input("Password: ")
# # if username == "admin" and (password == "1234" or password == "123456"):
# if username == "admin" and password in ["1234", "123456"]:
#     print("Login successful")
# else:
#     print("Get out! Hacker!")


# non-empty string is evaluated to True


def f2(a, b, c=0):
    return a * 100 + b * 10 + c


result = f2(3, 4)
print(result)

result = f2(b=4, a=3, c=5)
print(result)

result = f2(3, 4, 5)
print(result)

# year = 2024

# condition = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# print(condition)


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

year = 2100
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

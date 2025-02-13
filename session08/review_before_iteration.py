# score = 95

# if score >= 60:
#     print("Pass")
# elif score >= 90:
#     print("A")
# else:
#     print("Fail")


def check_grade(score):
    if score >= 60:
        return "Pass"
    # return immediately ends the function.

    if score >= 90:
        return "A"
    else:
        return "Fail"


def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"


# result = check_grade(95)
# print(result)

# result_2 = check_grade(55)
# print(result_2)


def f():
    """
    Just print hi
    """
    print("hi")
    return None


# result = f()


def calc(a, b, c=4):
    # return a * 10 + b
    return a * 100 + b * 10 + c


res_1 = calc(2, 5, 3)  # positional arguments
print(res_1)

res_2 = calc(b=5, a=2, c=3)  # keyword arguments
print(res_2)

res_3 = calc(2, 5) # For parameter c, it will be using the default value
print(res_3)
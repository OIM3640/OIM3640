def my_abs(x):
    """Return the absolute value of given number"""
    if x < 0:
        return -x
    else:
        return x


# Testing is important!
print(my_abs(10))
print(my_abs(0))
print(my_abs(-10.5))
def my_abs(x):
    """Return the absolute value of given number"""
    if x < 0:
        return -x
    else:
        return x


# Testing is important!
def main():
    print(my_abs(10))


if __name__ == "__main__":
    main()

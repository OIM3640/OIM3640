# i = 5
# while i > 0:
#     import time

#     print(i)

#     time.sleep(1)
#     i -= 1
# print("Happy New Year!")


def recursive_countdown(n):
    if n <= 0:
        print("Happy New Year!")
    else:
        print(n)
        import time

        time.sleep(1)
        recursive_countdown(n - 1)


# recursive_countdown(5)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# for i in range(1, 10):
#     print(fibonacci(i))


n = 5
while n != 0:
    print(n)
    n = n - 2
"""
5
3
1
-1
... and so on, an infinite loop
"""

# for i in range(4):
#     print('🧱'*i)


i = 0

while i < 4:
    print("🧱" * i)
    i += 1

for i in range(4):
    print("🧱" * i)


# Sum up 0 to 10


def sum_up(n):
    total = 0
    for i in range(n + 1):
        # print(f"In iteration {i}:")
        # print(f"  Before adding {i}, total = {total}")
        total += i
        # print(f"  After adding {i}, total = {total}")
        # print()
    return total


# result = sum_up(10)
# print(result)


def sum_up_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total + i  # This is an expression, not statement. It does nothing.
            total += i
    return total

def sum_up_even(n):
    total = 0
    for i in range(0, n + 1, 2):
        total += i
    return total

result = sum_up_even(10)
print(result)

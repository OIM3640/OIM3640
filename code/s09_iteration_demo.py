# Use for loop
# 1. when you know exactly how many times you want to iterate

for i in range(5):
    print("Hi")

# 2. iterating over a specific range of integers
for i in range(5):
    print("#" * i)


for i in range(0, 100, 3):
    print(i)

# 3. looping through elements in a collection or sequence (e.g., string, list, tuple, dictionary, set)

for letter in "Tauria":
    print(letter)

for num in [1, 2, 3, 4, 5]:
    print(num * 2)

for item in (10, 20, 30):
    print(item + 5)


# while

# creating an infinite loop

# while True:
#     game()

# the number of iterations is unknown and should continue until:
# while True:
#     game()
#     if something_happens:
#         break

# i = 5
# while i > 0:
#     import time

#     print(i)

#     time.sleep(1)
#     i -= 1
# print("Happy New Year!")

# until a break

# while True:
#     user_input = input("Enter a number (or 'q' to quit): ")
#     if user_input.lower() == "q":
#         print("Exiting the loop.")
#         break
#     print(f"You entered: {user_input}")


# while True:
#     username = input("Username: ")
#     password = input("Password: ")
#     if username == "admin" and password == "123456":
#         print("Login successful")
#         break
#     else:
#         print("Try again!")

# break: immediately exits the entire loop
# continue: skips the rest of the current iteration and moves to the next one.

for i in range(1, 10):
    if i % 3 == 0:
        continue
    print(i)

# print('break')
# for i in range(1, 10):
#     if i % 3 == 0:
#         break
#     print(i)


# print('continue')
# for i in range(1, 10):
#     if i % 3 == 0:
#         continue
#     print(i)




# print('Proceed!')


# for i in range(5):
#     print('🤣')


# for i in range(5):
#     print('🤣', end='')
# print()

# print("🤣" * 5)

# for i in range(1, 6):
#     print("🧱" * i)


# n = 5
# while n != 0:
#     print(n)
#     n = n - 2


# When to use what for loops (`for` vs. `while`)

# 1. Use `for`
# 1.1. when you know the exact number of iterations

# for i in range(4):
#     print('👍')

# i = 0
# while i < 4:
#     print('👍')
#     i += 1

# 1.2 when you need to iterate over a collection/sequence, such as a string, list, dict, tuple, set...

# for letter in 'George': # a string
#     print(letter)


# for number in [1, 2, 3, 4]: # a list
#     print(number ** 2)

# 2. Use while loop

# 2.1 when you need to create an infinite loop

# while True:
#     game()

# 2.2 When you don't know the exact number of iterations beforehand, and want to continue until
# 2.2.1 ... a specific condition is no longer True

# import time

# counter = 5
# while counter > 0:
#     print(counter)
#     time.sleep(1)
#     counter -= 1

# print("blast off!")

# 2.2.2 ... a break statement is met
# trials = 0
# while True:
#     if trials >= 5:
#         print('You have tried 5 times.')
#         break
#     trials += 1
#     print(f'Trial {trials}:')
#     password = input('Please enter your password: ')
#     if password == '123456':
#         print('You are logged in. Welcome!')
#         break
#     else:
#         print('Please try again.')


for i in range(5):
    print(f'Trial {i+1}: ')
    password = input('Please enter your password: ')
    if password == '123456':
        print('You are logged in. Welcome!')
        break
    else:
        print('Please try again.')
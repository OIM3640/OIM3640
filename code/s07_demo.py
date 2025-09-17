def is_even(x):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")


# is_even(10)
# is_even(7)

age = int(input("How old are you? "))

# if age >= 21:
#     print('Yes you can')
# elif age < 18:
#     print('You are too young! Get out of here!')
# else:
#     print('Sorry, you cannot.')

if age < 21:
    print("Sorry, you cannot.")
elif age < 18:
    print("You are too young! Get out of here!")
else:
    print("Yes, you can!")

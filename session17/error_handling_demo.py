print("A lot of tasks...")

# try:
#     number = int(input("Please enter a number: >> "))
#     result = 2025 / number
#     print(result)
# except ZeroDivisionError:
#     print("⚠️  You just entered 0!")
# except ValueError as e:
#     print('⚠️  You should enter an integer!')
#     print(type(e).__name__)
#     print(e)
# except:
#     print('Something wrong happend!')
# finally:
#     print('No matter what happens, we will get here.')


data = ['Aryan', 'George', 'Thomas', 2025, 'Khushi']

for name in data:
    try:
        print(name[0])
    except TypeError:
        print(f'{name} is not a string!')

print("Move on to the next task...")

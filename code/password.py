"""
You've been hired as a cybersecurity analyst for a major e-commerce platform, and your primary task is to improve the security of user accounts by identifying strong passwords and eliminating weak ones.

Recently, your team has received reports of user accounts being compromised due to weak, easily guessable passwords. After conducting a security audit, you have identified a list of commonly used passwords stored in a file called "common_passwords.txt", which you can access and download through a link (https://bit.ly/python-quiz-3)

The passwords in the file look like this:

mm44693avl$
kdOP
2kEqMWWFi
4NyTu0
gt$YrkPwTm8!g
…

Your Task:

Write a function, find_strong_passwords, that identifies strong passwords and returns them as a list. (If you are not yet familiar with lists, you can simply print out the strong passwords instead.) A password is considered "strong" if it meets all of the following conditions:
•	The password must contain at least one uppercase letter, one lowercase letter, and one digit.
•	The password must NOT contain two consecutive identical characters.
•	The password must be at least 12 characters long.

Note:
•	You might want to create “helper” functions to keep your code organized.
•	Use meaningful function and variable names to improve readability.
•	You can use the following scaffold code to help you get started:
f = open("data/common_passwords.txt") # Open the file "common_passwords.txt" that contains all the passwords, one per line.
for line in f: # Iterate through each line, where each line contains one password. Note: you should know that each line ends with a newline character ('\n').

"""


def contains_uppercase(s):
    """Return True if ..."""
    for c in s:
        if c.isupper():
            return True
    return False


def contains_upper_lower_digit(s):
    """Return True if ..."""
    upper_flag = False
    lower_flag = False
    digit_flag = False
    for c in s:
        if c.isupper():
            upper_flag = True
        elif c.islower():
            lower_flag = True
        elif c.isdigit():
            digit_flag = True
    return upper_flag and lower_flag and digit_flag


def find_strong_passwords():
    """
    find strong passwords and return them as a list
    """
    f = open("data/common_passwords.txt", "r")
    strong_password_list = []
    for line in f:
        # print(line)
        password = line.strip()
        # print(password)
        if len(password) > 12 and contains_uppercase(password):
            # Check for two consecutive identical characters
            if not any(
                password[i] == password[i + 1] for i in range(len(password) - 1)
            ):
                strong_password_list.append(password)
    return strong_password_list


strong_passwords = find_strong_passwords()
print(len(strong_passwords))

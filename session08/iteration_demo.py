# Sum up integers from 0 to 100

# result = 0 + 1 + 2 + 3 + ... + 10
# print(result)

def sum10():
    """
    Calculate the sum of integers from 0 to 10, return the sum
    """
    # Create a variable to hold some value, so we can return it in the end
    result = 0
    for i in range(11):
        print(f'Iteration {i}:')
        print(f'  Before adding {i}, the current result is {result}')
        # print(i)
        # in every iteration, we need to add i to result
        result = result + i

        print(f'  After adding {i}, the result becomes {result}')
        print()

    return result

# print(sum10())

# Create another function to calcuate the sum of integers from 0 to 100
def sum100():
    """
    Calculate the sum of integers from 0 to 100, return the sum
    """
    # Create a variable to hold some value, so we can return it in the end
    result = 0
    for i in range(101):
        print(f'Iteration {i}:')
        print(f'  Before adding {i}, the current result is {result}')
        # print(i)
        # in every iteration, we need to add i to result
        result = result + i

        print(f'  After adding {i}, the result becomes {result}')
        print()

    return result

# print(sum100())

# Create another function to sum up integers from 0 to n

def sum_up(n):
    """
    Calcuate the sum of integers from 0 to n, and return the sum
    """
    result = 0

    for i in range(n + 1):
        result += i # a shortcut of result = result + i

    return result


# print(sum_up(100))

def sum_odd(n):
    """
    Calcuate the sum of odd numbers from 0 to n, and return the sum
    """
    result = 0
    for i in range(n + 1):
        if i % 2 == 1: # i is an odd number
            result += i
    return result
    

print(sum_odd(100))
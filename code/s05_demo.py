import math


def print_double(number):
    """Print the double of the number
    It is not AI, it is called docstring

    number: int or float
    """
    result = number * 2
    print(result)


def calc_volume(radius):
    volume = (4 / 3) * math.pi * radius**3
    # print(volume)
    return volume

def double(number):
    return number * 2

# print the double of volume of sphere with radius 5
# calc_volume(5)
# result = calc_volume(5)
# print(result)
# print_double(result)

# # get sqrt of double of the volume
# result = double(calc_volume(5))
# print(math.sqrt(result))

# print(double(100))



print('Hi', end='#####')
print('Hello')
r1 = 1
r2 = 10
r3 = 2025

# area_1 = 3.14159 * r1 * r1
# area_2 = 3.14159 * r2 * r2

# print(area_1)
# print(area_2)


def calc_area(radius):
    """
    Calculate the area of a circle given its radius and return it.
    """
    pi = 3.14159
    area = pi * radius**2
    # print(area)
    # If the function does not explicitly return any value, it will return None.

    return area


# calc_area(r1)  # Calling the function
# calc_area(r2)
# calc_area(r3)

# Calculate the total area by summing up all the areas of three circles
area_1 = calc_area(r1) 
area_2 = calc_area(r2) 
area_3 = calc_area(r3)

# print(area_1)
print(area_1 + area_2 + area_3)


def double(x):
    """
    Return the double of the given value
    """
    return x * 2

print(double(20))


# Calcuate the area of a circle with double of a given radius. For example: if the radius is 3, calculate the area of circle with radius 3*2

r = 3

new_r = double(r)
new_area = calc_area(new_r)
print(new_area)

print(calc_area(double(r)))
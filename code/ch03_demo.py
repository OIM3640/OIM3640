import math

def calc_volume(radius): 
    volume = (4 / 3) * math.pi * radius**3
    print(volume)
    # return None


# calc_volume(5)
# calc_volume(10)
# # calc_volume()

# radius = 3
# print(radius)
# volume = 10
# print(volume)


for i in range(4):
    calc_volume(5)
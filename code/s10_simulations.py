"""
Write a program that simulates a dice experiment:
- Run the simulation 10 times.
- In each simulation, roll 100 dice (🎲🎲🎲🎲🎲🎲🎲🎲🎲...).
- After each simulation, display the sum of all 100 rolls.
"""

"""
I will create 2 functions

1. Repeat simultion (10 times)
   1. for loop, repeat function 2

2. One simultion: rolling 100 dice, summing up all the faces
   1. initialize a variable `total` to store the sum
   2. Loop the following things 100 times:
      1. get a random integer (1 - 6) (remember to import random)
      2. add the random integer to total
   3. print the final total
"""
import random


def simulation(n, m=6):
    """
    Simulate rolling n dice with m sides,
    """
    # print("We found the sum!")  # Fake it till make it
    total = 0
    for i in range(n):
        random_number = random.randint(1, m)
        # print(chr(9856 + random_number - 1), end=" ")
        total = total + random_number
    print(total, total/n)


def repeat_simulations(n_times=10, n_dice=100):
    """"""
    for i in range(n_times):
        simulation(n_dice)


repeat_simulations(5, 1_000_000)


# Try to print character of dice

# calcute the avergage

# see how many simulations to get average 4

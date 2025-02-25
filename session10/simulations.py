# Create function(s) that execute a simulation 10 times. Within each simulation, roll 100 dice (🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲...) and display the resulting sum.

"""
I will create 2 functions

Function 1: run one simulation

Function 2: repeat simulation 10 times
"""

def roll_dice():
    """One simulation"""
    total = 0

    
    print(f'Sum = {total}')  # Fake it till make it!



def repeat_simulation():
    """repeat the simulation 10 times"""
    for i in range(10):
        roll_dice()


repeat_simulation()
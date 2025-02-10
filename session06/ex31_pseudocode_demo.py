import turtle

from turtle_shape import square


def spiral(t, n):
    """
    Asks user to enter the initial length,
    draws a spiral shape - that is drawing a square multiple times,
    after one square, turn 5 degrees

    t: a turtle
    n: int, number of squares to draw for the spiral
    """
    # Pseudocode:
    # 1. Prompt the user to enter the initial length of the square's side.
    # 2. Convert the input to an integer and store it as `length`.
    # 3. Repeat n times:
    #    a. Call the function `square(t, length)` to draw a square of side `length`.
    #    b. Rotate the turtle right by 5 degrees.
    #    (Optional) If the spiral should grow/shrink, adjust `length`.
    
    length = input("Enter the length of square's side: ")
    length = int(length)
    for i in range(n):
        square(t, length)
        t.right(5)


def main():
    turtle.speed(0)

    leo = turtle.Turtle()
    spiral(leo, 10)
    turtle.mainloop()


if __name__ == "__main__":
    main()

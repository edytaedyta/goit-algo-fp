import turtle
import math

def draw_pythagorean_tree(level, length):
    if level == 0:
        turtle.forward(length)
        turtle.backward(length)
        return

    # Draw the trunk
    turtle.forward(length)

    # Draw the left branch
    turtle.left(45)
    draw_pythagorean_tree(level - 1, length * math.sqrt(2) / 2)
    turtle.right(45)

    # Draw the right branch
    turtle.right(45)
    draw_pythagorean_tree(level - 1, length * math.sqrt(2) / 2)
    turtle.left(45)

    # Move back to the original position
    turtle.backward(length)

# Initial setup
turtle.speed('fastest')
turtle.left(90)  # Start pointing up
turtle.color("red")

# Draw the Pythagorean tree
draw_pythagorean_tree(5, 100)  # Example: level 5, length 100

# Complete the drawing
turtle.done()
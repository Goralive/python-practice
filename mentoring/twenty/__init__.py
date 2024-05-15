import turtle

# Set up the screen
turtle.Screen()
turtle.bgcolor("lightblue")

# Create a turtle named "alex"
alex = turtle.Turtle()
alex.color("red")

# Make "alex" draw a square
for _ in range(4):
    alex.forward(100)  # Move alex forward by 100 units
    alex.right(90)  # Turn alex right by 90 degrees

# Finish
turtle.done()

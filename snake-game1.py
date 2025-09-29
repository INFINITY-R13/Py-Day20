# snake-game1.py

# Import necessary classes from the turtle module and the time module.
from turtle import Turtle, Screen
import time
# Import the Snake class from the snake.py file.
from snake import Snake 


# --- Screen Setup ---
# Create a new screen object.
screen = Screen()
# Set the dimensions of the screen.
screen.setup(width=600, height=600)
# Set the background color of the screen.
screen.bgcolor("black")
# Set the title of the window.
screen.title("My Snake Game")
# Turn off automatic screen updates. This allows for smoother animation.
screen.tracer(0)

# --- Game Objects ---
# Create an instance of the Snake class.
snake = Snake()

# --- Keyboard Bindings ---
# Start listening for keyboard inputs.
screen.listen()
# Bind the arrow keys to the corresponding methods in the Snake class.
screen.onkey(snake.up, "Up")       # Up arrow key calls the snake.up() method.
screen.onkey(snake.down, "Down")   # Down arrow key calls the snake.down() method.
screen.onkey(snake.left, "Left")     # Left arrow key calls the snake.left() method.
screen.onkey(snake.right, "Right")   # Right arrow key calls the snake.right() method.

# --- Main Game Loop ---
# Flag to keep the game running.
game_is_on = True
while game_is_on:
    # Update the screen to show the snake's new position.
    screen.update()
    # Pause the loop for a short duration to control the speed of the snake.
    time.sleep(0.1)
    
    # Move the snake forward.
    snake.move()

# --- Exit ---
# The screen will close when clicked.
screen.exitonclick()
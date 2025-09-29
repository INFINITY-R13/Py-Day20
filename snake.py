# snake.py

# Import the Turtle class.
from turtle import Turtle

# --- Constants ---
# Define the initial positions of the first three snake segments.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Define the distance the snake moves in each step.
MOVE_DISTANCE = 20
# Define heading constants for clarity. (Turtle's heading is in degrees).
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """A class to represent the snake in the game."""

    def __init__(self):
        """Initializes the snake's attributes."""
        # A list to hold all the turtle objects (segments) that make up the snake.
        self.segments = []
        # Create the initial snake body.
        self.create_snake()
        # A reference to the first segment (the head) for easier control.
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake body with three segments."""
        for position in STARTING_POSITIONS:
            # Create a new square-shaped turtle for each segment.
            new_segment = Turtle("square")
            new_segment.color("white")
            # Lift the pen to move without drawing lines.
            new_segment.penup()
            # Move the segment to its starting position.
            new_segment.goto(position)
            # Add the new segment to our list of segments.
            self.segments.append(new_segment)
        
    def move(self):
        """Moves the snake forward by one step."""
        # This loop makes each segment follow the one in front of it.
        # It starts from the last segment and goes to the second one (index 1).
        # range(start, stop, step)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Get the coordinates of the segment in front.
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Move the current segment to that position.
            self.segments[seg_num].goto(new_x, new_y)
        # After all segments have followed, move the head forward.
        self.head.forward(MOVE_DISTANCE)

    # --- Directional Control Methods ---
    def up(self):
        """Sets the snake's heading to UP (90 degrees) if it's not currently moving DOWN."""
        # This prevents the snake from reversing into itself.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)        

    def down(self):
        """Sets the snake's heading to DOWN (270 degrees) if it's not currently moving UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 

    def left(self):
        """Sets the snake's heading to LEFT (180 degrees) if it's not currently moving RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 

    def right(self):
        """Sets the snake's heading to RIGHT (0 degrees) if it's not currently moving LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
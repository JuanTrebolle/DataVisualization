"""A random walk is a path that has no clear direction but is 
    determined by a series of random decisions, each of which 
    is left entirely to chance"""

from random import choice

class RandomWalk():
    """A class to generate random walks"""

    def __init__(self, num_points=500):
        """Initialize attributes of a walk."""
        self.num_points = num_points # Stores the number of points in the walk

        # All walks start at (0.0)
        self.x_values = [0] # Stores x-coordinate values of each point in the walk
        self.y_values = [0] # Stores y-coordinate values of each point in the walk

    """To make random decisions, we'll store possible choices in 
        a list and use choice() to decide which choice to use each
        time a decision is made. Then we set the default number of
        points to 5000, and then we make 2 lists to store the values,
        starting at (0,0)."""

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1]) # 1 for right, -1 for left
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1]) # 1 for right, -1 for left
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.(x=0, y=0)
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

            """The main part of this method tells Python how to simulate
            4 random decision: 
                1.- Will the walk go right or left?
                2.- How far will it go in that direction?
                3.- Will it go up or down?
                4.- How far will it go in that direction"""
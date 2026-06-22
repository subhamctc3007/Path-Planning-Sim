import pygame

WHITE = (255, 255, 255) # Open
BLACK = (0, 0, 0)       # Obstacle

GREEN = (0, 255, 0)     # Start Position
RED = (255, 0, 0)       # Goal Position

class Node:
    """Node object for defining individual squares on the grid"""
    def __init__(self, row, col, size):
        self.row = row
        self.col = col

        self.x = col * size
        self.y = row * size

        self.size = size
        self.color = WHITE

    def draw(self, win):
        pygame.draw.rect(
            win,
            self.color,
            (self.x, self.y, self.size, self.size)
        )

    def is_obstacle(self):
        return self.color == BLACK
    
    def make_obstacle(self):
        self.color = BLACK

    def make_start(self):
        self.color = GREEN

    def make_goal(self):
        self.color = RED

    def reset(self):
        self.color = WHITE

import pygame

WHITE = (255, 255, 255) # Open
BLACK = (0, 0, 0)       # Obstacle

GREEN = (0, 255, 0)     # Start Position
RED = (255, 0, 0)       # Goal Position
BLUE = (0, 0, 255)      # Open
CYAN = (64, 224, 208)   # Visited
YELLOW = (255, 255, 0)  # Final path

class Node:
    """Node object for defining individual squares on the grid"""
    def __init__(self, row, col, size):
        self.row = row
        self.col = col

        self.x = col * size
        self.y = row * size

        self.size = size
        self.color = WHITE

        self.neighbors = []

    def draw(self, win):
        pygame.draw.rect(
            win,
            self.color,
            (self.x, self.y, self.size, self.size)
        )

    def update_neighbors(self, grid):
        self.neighbors = []
        total_rows = len(grid)

        # DOWN
        if (self.row < total_rows - 1 and not grid[self.row + 1][self.col].is_obstacle()):
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if (self.row > 0 and not grid[self.row - 1][self.col].is_obstacle()):
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if (self.col < total_rows - 1 and not grid[self.row][self.col + 1].is_obstacle()):
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if (self.col > 0 and not grid[self.row][self.col - 1].is_obstacle()):
            self.neighbors.append(grid[self.row][self.col - 1])

    def get_pos(self):
        return self.row, self.col
    
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

    def make_open(self):
        self.color = BLUE

    def make_closed(self):
        self.color = CYAN

    def make_path(self):
        self.color = YELLOW

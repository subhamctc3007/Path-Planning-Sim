import pygame
import random

# custom modules
from node import Node
from algorithms.bfs import bfs

WIDTH = 800
ROWS = 40

pygame.init()

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Planning Visualizer")

GREY = (128, 128, 128)
WHITE = (255, 255, 255)

CELL_SIZE = WIDTH // ROWS

def make_grid():
    # creates a 40x40 list of node objects
    grid = []
    for row in range(ROWS):
        grid.append([])
        for col in range(ROWS):
            node = Node(row, col, CELL_SIZE)
            grid[row].append(node)

    return grid

def generate_random_grid():
    # Takes the 40x40 list and decides properties of each square,
    # wether it will be a free space or an obstacle
    grid = make_grid()
    obstacle_probability = 0.25

    free_nodes = [] 
    for row in grid:
        for node in row:
            if random.random() < obstacle_probability:
                node.make_obstacle()
            else:
                free_nodes.append(node)

    start = random.choice(free_nodes)
    start.make_start()
    free_nodes.remove(start) # coz goal pos may overide it

    goal = random.choice(free_nodes)
    goal.make_goal()

    return grid, start, goal

def draw_grid_lines(win):
    # draws the grid lines on the existing white canvas
    for i in range(ROWS):
        pygame.draw.line(
            win,
            GREY,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE)
        )

        pygame.draw.line(
            win,
            GREY,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, WIDTH)
        )

def create_canvas(win, grid):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid_lines(win)
    pygame.display.update()

def main():
    grid, start, goal = generate_random_grid()

    running = True
    while running:
        create_canvas(WIN, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid, start, goal = generate_random_grid()

                if event.key == pygame.K_SPACE:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    bfs(lambda: create_canvas(WIN, grid), start, goal)

    pygame.quit()

if __name__ == "__main__":
    main()
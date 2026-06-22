from collections import deque
import pygame

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def bfs(draw, start, goal):
    queue = deque([start])
    visited = {start}
    came_from = {}

    while queue:
        # pygame window updates
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.popleft()
        if current == goal:
            reconstruct_path(came_from, goal, draw)
            goal.make_goal()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
                if neighbor != goal:
                    neighbor.make_open()

        if current != start:
            current.make_closed()

        draw()

    return False
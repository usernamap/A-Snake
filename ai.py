# ai.py
import pygame
from game_config import *


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0


def astar(start, end, snake_body, grid_size):
    open_list = []
    closed_list = []

    start_node = Node(start)
    end_node = Node(end)
    open_list.append(start_node)

    directions = [
        pygame.math.Vector2(0, -1),
        pygame.math.Vector2(0, 1),
        pygame.math.Vector2(-1, 0),
        pygame.math.Vector2(1, 0),
    ]

    while open_list:
        current_node = open_list[0]
        current_index = 0
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for direction in directions:
            new_position = (
                current_node.position[0] + int(direction.x),
                current_node.position[1] + int(direction.y),
            )

            if (
                new_position[0] > (grid_size - 1)
                or new_position[0] < 0
                or new_position[1] > (grid_size - 1)
                or new_position[1] < 0
            ):
                continue

            if new_position in snake_body:
                continue

            new_node = Node(new_position, current_node)
            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child.position == closed_child.position:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                (child.position[1] - end_node.position[1]) ** 2
            )
            child.f = child.g + child.h

            for open_node in open_list:
                if child.position == open_node.position and child.g > open_node.g:
                    continue

            open_list.append(child)

    return None

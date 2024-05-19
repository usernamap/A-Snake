import heapq
import numpy as np
from collections import deque
import pygame
from game_config import *


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def astar(start, end, snake_body, grid_size):
    open_list = []
    closed_list = set()
    start_node = Node(start)
    end_node = Node(end)
    heapq.heappush(open_list, start_node)
    directions = [
        np.array([0, -1]),
        np.array([0, 1]),
        np.array([-1, 0]),
        np.array([1, 0]),
    ]

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)
        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        for direction in directions:
            new_position = tuple(np.array(current_node.position) + direction)
            if (
                new_position[0] < 0
                or new_position[0] >= grid_size
                or new_position[1] < 0
                or new_position[1] >= grid_size
                or new_position in closed_list
                or any(np.array_equal(new_position, segment) for segment in snake_body)
            ):
                continue
            new_node = Node(new_position, current_node)
            new_node.g = current_node.g + 1
            new_node.h = (new_position[0] - end_node.position[0]) ** 2 + (
                new_position[1] - end_node.position[1]
            ) ** 2
            new_node.f = new_node.g + new_node.h
            if any(
                open_node.position == new_node.position and new_node.g > open_node.g
                for open_node in open_list
            ):
                continue
            heapq.heappush(open_list, new_node)
    return None


def bfs(start, end, snake_body, grid_size):
    queue = deque([Node(start)])
    closed_list = set()
    directions = [
        np.array([0, -1]),
        np.array([0, 1]),
        np.array([-1, 0]),
        np.array([1, 0]),
    ]

    while queue:
        current_node = queue.popleft()
        closed_list.add(current_node.position)
        if current_node.position == end:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        for direction in directions:
            new_position = tuple(np.array(current_node.position) + direction)
            if (
                new_position[0] < 0
                or new_position[0] >= grid_size
                or new_position[1] < 0
                or new_position[1] >= grid_size
                or new_position in closed_list
                or any(np.array_equal(new_position, segment) for segment in snake_body)
            ):
                continue
            new_node = Node(new_position, current_node)
            if new_node.position not in closed_list:
                queue.append(new_node)
    return None


def follow_tail(snake_body, grid_size):
    tail = snake_body[-1]
    queue = deque([Node(snake_body[0])])
    closed_list = set()
    directions = [
        np.array([0, -1]),
        np.array([0, 1]),
        np.array([-1, 0]),
        np.array([1, 0]),
    ]

    while queue:
        current_node = queue.popleft()
        closed_list.add(current_node.position)
        if current_node.position == tail:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        for direction in directions:
            new_position = tuple(np.array(current_node.position) + direction)
            if (
                new_position[0] < 0
                or new_position[0] >= grid_size
                or new_position[1] < 0
                or new_position[1] >= grid_size
                or new_position in closed_list
                or any(np.array_equal(new_position, segment) for segment in snake_body)
            ):
                continue
            new_node = Node(new_position, current_node)
            if new_node.position not in closed_list:
                queue.append(new_node)
    return None

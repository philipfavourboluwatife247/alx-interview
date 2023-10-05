#!/usr/bin/python3

from collections import deque
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be
    unlocked starting from the first box.

    Args:
        boxes (List[List[int]]): A list
        of lists, where each inner list
        represents a box and contains keys
        to other boxes.

    Returns:
        bool: True if all boxes can be
        opened, False otherwise.
    """

    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited except the empty ones
    return all(visited) and all(
            visited[i] or not boxes[i] for i in range(1, n)
    )

# Example usage:
# boxes1 = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes1))
#
# boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes2))
#
# boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes3))

#!/usr/bin/python3


def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n  # Initialize a list to keep track of visited boxes
    stack = [0]  # Start with the first box (box 0) which is unlocked

    while stack:
        current_box = stack.pop()
        visited[current_box] = True  # Mark the current box as visited

        # Check the keys in the current box
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                stack.append(key)  # Add the unvisited box to the stack

    # If all boxes are visited, return True; otherwise, return False
    return all(visited)

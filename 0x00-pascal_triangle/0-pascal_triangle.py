#!/usr/bin/python3
""" Pascal Triangle function
    The function iterates each row and
    add items from previous rows to form the new row
"""


def pascal_triangle(n):
    """ Function to develop pascal triangle"""
    triangle = []
    i = 0   # Initialize row index
    if (n <= 0):
        return []
    while i < n:
        row = [1]   # Start each row with 1
        if triangle:   # If not the first row
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)  # End each row with 1
        triangle.append(row)
        i += 1

    return triangle

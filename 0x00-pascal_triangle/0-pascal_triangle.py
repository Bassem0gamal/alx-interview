#!/usr/bin/python3
""" creating pascal's triangle """

def pascal_triangle(n):
    """ A function to create pascal's triangle """

    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        triangle_row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle_row.append(1)
            else:
                triangle_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(triangle_row)
    return triangle
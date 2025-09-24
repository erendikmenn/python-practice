# Task 9: Transpose
"""
Scenario: Your task is to transpose a matrix, swapping 
its rows and columns.
"""
import numpy

grades = numpy.array([[90, 85], 
                     [70, 75], 
                     [88, 92]])

# Transpose the matrix
transposed_grades = grades.T

print(transposed_grades)
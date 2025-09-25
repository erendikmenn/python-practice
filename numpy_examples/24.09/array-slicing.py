# Task 3: Array Slicing
"""
Scenario: Given a 2D array, your task is to select 
the second column (index 1).
"""
import numpy

a = numpy.array([[10, 20, 30], 
                 [11, 21, 31], 
                 [12, 22, 32], 
                 [13, 23, 33], 
                 [14, 24, 34]])

# Select the second column (index 1)
second_column = a[:, 1]

print(second_column)
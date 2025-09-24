# Task 5: Concatenate Arrays
"""
Scenario: Your task is to combine two arrays row-wise 
(stacking them vertically) to create a single array.
"""
import numpy

a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[7, 8, 9]])

# Concatenate arrays along rows (axis=0)
combined_array = numpy.concatenate((a, b), axis=0)

print(combined_array)
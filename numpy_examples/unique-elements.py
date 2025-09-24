# Task 7: Unique Elements
"""
Scenario: Your task is to find the unique elements in an array, 
removing any duplicates.
"""
import numpy

ages = numpy.array([22, 35, 22, 41, 35, 28, 41, 22])

# Find the unique elements
unique_ages = numpy.unique(ages)

print(unique_ages)
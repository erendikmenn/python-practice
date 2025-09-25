# Task 6: Boolean Indexing
"""
Scenario: Your task is to filter an array of grades to select only 
the elements that are greater than or equal to 50.
"""
import numpy

grades = numpy.array([75, 42, 88, 50, 91, 34, 65])

# Select grades that are 50 or higher
passing_grades = grades[grades >= 50]

print(passing_grades)
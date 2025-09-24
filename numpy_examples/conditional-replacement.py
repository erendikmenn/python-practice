# Task 10: Conditional Replacement with 'where'
"""
Scenario: Your task is to replace all negative values in an array 
with 0, while keeping non-negative values as they are.
"""
import numpy

temps = numpy.array([22.5, 23.1, -99.0, 21.9, -1.5, 24.0])

# Replace negative values with 0, leave others unchanged
cleaned_temps = numpy.where(temps < 0, 0, temps)

print(cleaned_temps)
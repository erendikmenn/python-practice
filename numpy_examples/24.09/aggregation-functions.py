# Task 4: Aggregation Functions (sum)
"""
Scenario: Given a 2D array representing sales, your task is to compute 
the sum of each column to find the total sales per day.
"""
import numpy

sales = numpy.array([[10, 15, 20, 25], 
                     [5, 8, 12, 10], 
                     [7, 9, 11, 13]])

# Sum along the columns (axis=0)
column_sums = sales.sum(axis=0)

print(column_sums)
# Task 1: Array Creation and Data Type
"""
Scenario: You are given a space-separated list of integers. 
Your task is to convert these numbers into a NumPy array of floats.
"""
import numpy

# Input: 1 2 3 4 5
input_list = input().split()
result = numpy.array(input_list, dtype=float)

print(result)
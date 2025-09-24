# Task 8: Element-wise Operations
"""
Scenario: Convert an array of prices from USD to a local currency 
by multiplying by an exchange rate (e.g., 30), and then 
add a 20% sales tax (multiply by 1.2).
"""
import numpy

prices_usd = numpy.array([10, 20, 50, 100])

# First, convert to local currency by multiplying by 30
# Then, add a 20% tax by multiplying by 1.2
final_prices = prices_usd * 30 * 1.2

print(final_prices)
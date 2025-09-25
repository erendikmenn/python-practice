import numpy as np

# STAGE 1: Create a random array with a normal distribution
# We are creating an array with 20 elements, a mean of 50, and a standard deviation of 10.
mean_target = 50
std_dev_target = 10
num_elements = 20

original_array = np.random.normal(loc=mean_target, scale=std_dev_target, size=num_elements)

print("--- ORIGINAL DATA ---")
print("Generated Original Array:")
# Rounding the numbers for better readability.
print(np.round(original_array, 2))
print("-" * 25)

# STAGE 2: Define and find the outliers
# First, we calculate the actual mean and standard deviation of the array we created.
# These values will be very close to our target values of 50 and 10.
array_mean = original_array.mean()
array_std_dev = original_array.std()

print(f"Array's Actual Mean: {array_mean:.2f}")
print(f"Array's Actual Standard Deviation: {array_std_dev:.2f}")
print("-" * 25)

# We are defining our "Outlier" threshold.
# Values that are more than 2 standard deviations away from the mean will be considered outliers.
outlier_threshold = 2 * array_std_dev

# We create a "boolean mask" to identify the outliers.
# Condition: Is the distance of a number from the mean greater than the threshold?
outlier_mask = np.abs(original_array - array_mean) > outlier_threshold

# Let's find and print the outliers themselves using the mask.
# This array will be empty if there are no outliers.
detected_outliers = original_array[outlier_mask]

print("Detected Outliers:")
if detected_outliers.size == 0:
    print("No outliers were found.")
else:
    print(np.round(detected_outliers, 2))
print("-" * 25)

# STAGE 3: Replace outliers with the mean value
# It's best practice to work on a copy to avoid modifying the original array.
cleaned_array = original_array.copy()

# Using the boolean mask, we select the positions of the outliers
# and assign the array's mean value to these positions.
cleaned_array[outlier_mask] = array_mean

# STAGE 4: Show the results
print("\n--- CLEANED DATA ---")
print("New Array with Outliers Replaced by Mean:")
print(np.round(cleaned_array, 2))
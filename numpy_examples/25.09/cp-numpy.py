import numpy as np

arr_X = np.array([1,2,3])
arr_Y = np.array([4,5,6])

arr_X_plus_5 = arr_X+5
arr_Y_times_2 = arr_Y*2

print(arr_X_plus_5+arr_Y_times_2)

arr_X_copy = arr_X.copy()
arr_X_copy[0] = 99

print(arr_X_copy)
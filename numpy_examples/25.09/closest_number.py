import numpy as np

arr = np.arange(0,101,5)

target = 63

temp = 0

for i in range(0,len(arr)):
    if abs(arr[i] - target) < abs(arr[i+1] - target):
        print(arr[i])
        break
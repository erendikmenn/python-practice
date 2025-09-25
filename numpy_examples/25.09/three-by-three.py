import numpy as np

arr = np.arange(0,25)

new_arr = arr.reshape(5,5)

for i in range(1,4):
    new_arr[1:4,i] = 0

print(new_arr)
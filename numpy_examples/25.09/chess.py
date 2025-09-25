import numpy as np

arr = np.arange(0,64)
new_arr = arr.reshape(8,8)

for i in range(0,8):
    for j in range(0,8):
        if i % 2 == 0:
            if j % 2 == 0:
                new_arr[i][j] = 0
            else:
                new_arr[i][j] = 1
        elif i % 2 != 0:
            if j % 2 == 0:
                new_arr[i][j] = 1
            else:
                new_arr[i][j] = 0

print(new_arr)
        
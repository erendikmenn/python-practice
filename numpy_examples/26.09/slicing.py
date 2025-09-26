import numpy as np

arr = np.arange(0,15)

new_arr = arr.reshape(3,5)

sub_arr = new_arr[0:2,2:4]

print(sub_arr)
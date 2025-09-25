import numpy as np

arr = np.random.randint(0,100,size=16)
new_arr = arr.reshape(4,4)

print(new_arr)

minV = new_arr.min()
maxV = new_arr.max()

for i in range(0,4):
    for j in range(0,4):
        new_arr[i,j] = ((new_arr[i,j]-minV)/(maxV-minV))

print(new_arr)
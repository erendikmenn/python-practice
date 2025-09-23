import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    liste = numpy.array(arr,float)
    return(liste[::-1]) # Returns list backwards
    

arr = input().strip().split(' ') # Takes input and seperates it with space.
result = arrays(arr)
print(result)
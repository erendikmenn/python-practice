import numpy as np

arr = np.random.randint(0,100,size=12) # 0-100 arasında 12 tane random sayı.
new = arr.reshape(4,3)

print(new)

print(new > 50) #50'den büyük değerleri kontrol eder.

bigger = new[new>50] #50'den büyük değerleri bigger'a kaydeder.

print(bigger)


import numpy as np
import pandas as pd

arr = np.random.randint(0,100,size=(4,3))
df = pd.DataFrame(arr,columns=["A","B","C"])

print(df)

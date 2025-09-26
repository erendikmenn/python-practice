import numpy as np
import pandas as pd

exp ={
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan]
}

df = pd.DataFrame(exp)

print(df.isnull())

import numpy as np
import pandas as pd

exp = {
    "A": [10,20,30,40,50]
}

df = pd.DataFrame(exp)

print(df.describe())
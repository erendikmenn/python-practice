import numpy as np
import pandas as pd

exp = {
    "Notlar": [10,20,30,40,50,60]
}

df = pd.DataFrame(exp)
df["Karekök"] = np.sqrt(df["Notlar"])

print(df)
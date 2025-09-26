import numpy as np
import pandas as pd

exp = {
    'Isim': ['Can', 'Ece', 'Ada'],
    'Puan': [85, 92, 78]
}

df = pd.DataFrame(exp)
print(df)
print(df.sort_values("Puan"))
print(df)
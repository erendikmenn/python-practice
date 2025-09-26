import numpy as np
import pandas as pd

exp = {
    'Sehir': ['Ankara', 'İstanbul', 'İzmir', 'Ankara', 'Bursa', 'İstanbul']
    }

df = pd.DataFrame(exp)

print(df["Sehir"].value_counts())
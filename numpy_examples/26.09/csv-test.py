import numpy as np
import pandas as pd

exp = {
    'Isim': ['Can', 'Ece', 'Ada'],
    'Puan': [85, 92, 78]
}

df = pd.DataFrame(exp)

sorted = df.sort_values("Puan")

sorted.to_csv("ogrenci_puanlari.csv")
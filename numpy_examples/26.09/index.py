import pandas as pd

exp = {
    "Ürün" : ['Kalem', 'Defter', 'Silgi'],
    'Fiyat': [5, 15, 2],
    'Stok': [100, 50, 200]
}

df = pd.Series(exp)

print(df.iloc[1])
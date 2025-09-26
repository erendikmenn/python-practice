import pandas as pd

exp = {'Ürün': ['Elma', 'Armut'], 'Fiyat': [8, 10], 'Adet': [5, 10]}

df = pd.DataFrame(exp)

df["Toplam Tutar"] = df["Fiyat"]*df["Adet"] 

print(df)
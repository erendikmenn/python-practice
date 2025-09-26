import pandas as pd

exp = {
    "Isim":["Can","Ece","Ada"],
    "Puan":[85,92,78]
}

df = pd.Series(exp)

new = df.head(2)

print(new)
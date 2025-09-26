import pandas as pd

exp = {
    "Ürün":["Test-1","Test-2"],
    "Fiyat":["Test-3","Test-4"],
    "Stok":["Test-5","Test-6"]
}

df = pd.Series(exp)

print(df[["Ürün","Stok"]])
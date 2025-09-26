import pandas as pd

veri = {
    'Sipariş ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Ürün Adı': ['Laptop', 'Klavye', 'Mouse', 'Monitör', 'Klavye', 'Laptop', 'Kulaklık', 'Mouse', 'Klavye', 'Webcam'],
    'Adet': [1, 2, 3, 1, 1, 1, 2, 2, 1, 1],
    'Birim Fiyat (TL)': [15000, 750, 250, 4000, 750, 16500, 1200, 250, 800, 500]
}

df = pd.DataFrame(veri)

df["Toplam Gelir"] = df["Adet"] * df["Birim Fiyat (TL)"] #2

print(df.value_counts("Ürün Adı")) #3

toplam_gelirler = df.groupby("Ürün Adı")["Toplam Gelir"].sum()

en_cok_getiren_urun = toplam_gelirler.idxmax()

print(f"En çok gelir getiren ürün: {en_cok_getiren_urun}")




"""
top = 0
for i in range(0,10):
    if df["Ürün Adı"][i] == "Klavye":
        top += df["Toplam Gelir"][i]

print(f"Klavye'den elde edilen gelir toplam = {top}TL'dir.") #4

"""




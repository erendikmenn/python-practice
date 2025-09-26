import pandas as pd

exp = {
    "Isim": ["Ali","Ayşe","Veli","Fatma"],
    "Yas": [19,25,35,50],
    "Sehir": ["Izmir","Istanbul","Ankara","Bursa"]
}

df = pd.DataFrame(exp)

filtered = df[df["Yas"] < 30]

print(filtered)
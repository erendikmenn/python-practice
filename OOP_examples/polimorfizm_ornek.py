class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        # Bu metot alt sınıflar tarafından override edilmek için tasarlanmıştır.
        raise NotImplementedError("Bu metot alt sınıflarda uygulanmalıdır.")

class Kedi(Hayvan):
    def ses_cikar(self):
        return f"{self.isim}: Miyav!"

class Kopek(Hayvan):
    def ses_cikar(self):
        return f"{self.isim}: Hav hav!"

class Kus(Hayvan):
    def ses_cikar(self):
        return f"{self.isim}: Cik cik!"

# --- Polimorfizmin Kullanımı ---

# Farklı sınıflardan nesneler oluşturalım
kedi = Kedi("Tekir")
kopek = Kopek("Karabaş")
kus = Kus("Maviş")

# Tüm nesneleri bir listede toplayalım
hayvanlar = [kedi, kopek, kus]

# Döngü içinde her bir hayvanın nesne tipine bakmaksızın
# aynı isimdeki metodu çağırıyoruz.
# Python, her nesnenin kendi sınıfına ait olan `ses_cikar` metodunu çalıştıracaktır.
print("Hayvanat Bahçesi Sesleri:")
for hayvan in hayvanlar:
    print(hayvan.ses_cikar())

# Bu yapı sayesinde, gelecekte yeni bir Hayvan alt sınıfı (örn: Aslan) eklediğimizde
# bu döngüyü değiştirmemize gerek kalmaz. Sadece yeni sınıfı listeye eklememiz yeterlidir.
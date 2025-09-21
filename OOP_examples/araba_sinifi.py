# -*- coding: utf-8 -*-

class Araba:
    """
    Bu sınıf, bir arabanın temel özelliklerini ve işlevlerini temsil eder.
    Nitelikler (attributes): marka, model, yil, renk, hiz
    Metotlar (methods): hizlan, yavasla, durumu_goster
    """

    def __init__(self, marka, model, yil, renk):
        """
        Araba sınıfının yapıcı metodu (constructor).
        Yeni bir Araba nesnesi oluşturulduğunda bu metot otomatik olarak çalışır.
        """
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk
        self.hiz = 0  # Başlangıç hızı 0 olarak ayarlandı

    def hizlan(self, deger):
        """Arabanın hızını belirtilen değer kadar artırır."""
        self.hiz += deger
        print(f"{self.marka} {self.model} hızlanıyor... Yeni hız: {self.hiz} km/s")

    def yavasla(self, deger):
        """Arabanın hızını belirtilen değer kadar azaltır."""
        if self.hiz >= deger:
            self.hiz -= deger
        else:
            self.hiz = 0
        print(f"{self.marka} {self.model} yavaşlıyor... Yeni hız: {self.hiz} km/s")

    def durumu_goster(self):
        """Arabanın anlık durumunu ekrana yazdırır."""
        return f"Marka: {self.marka}\nModel: {self.model}\nYıl: {self.yil}\nRenk: {self.renk}\nHız: {self.hiz} km/s"

# --- Sınıfın Kullanımı ---

# Araba sınıfından bir nesne (instance) oluşturalım
araba1 = Araba("Ford", "Mustang", 2022, "Kırmızı")

# Nesnenin durumunu gösterelim
print("--- Araba 1 Bilgileri ---")
print(araba1.durumu_goster())
print("\n")

# Metotları kullanarak nesneyle etkileşime girelim
araba1.hizlan(50)
araba1.hizlan(30)
araba1.yavasla(20)

print("\n--- Son Durum ---")
print(araba1.durumu_goster())
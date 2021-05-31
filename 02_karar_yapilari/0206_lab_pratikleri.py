"""
sayi1=int(input("lütfen 1. sayıyı giriniz:"))
sayi2=int(input("lütfen 2. sayıyı giriniz:"))
if sayi1>sayi2:
    print(f"{sayi1}>{sayi2}")
"""

"""
bakiye = 5000 
kullaniciEFT = int(input("Ne kadar transfer edeceksiniz (TL) : "))
bankaAdi = "Halk"
bankaAdi2 = "Halk"
if bankaAdi != bankaAdi2 :
    kullaniciEFT *= 1.05
print(f"Şuanki bakiyeniz → {bakiye - kullaniciEFT}")
"""

"""
biletFiyati = float(input("lütfen bilet fiyatını giriniz:\t"))
bavulAgirligi = float (input("lütfen bavul ağırlığını giriniz:\t"))
ekUcret = 7.5
if bavulAgirligi >15:
    biletFiyati += (bavulAgirligi-15)* ekUcret
print(f"toplam ücret:{biletFiyati*1.18} ")
"""

# region ornek_4
"""
sayi = int(input("lütfen sayı giriniz "))
if sayi<0:
    sayi *= -1
print(f"sayının mutlak değeri {sayi}")
"""
# endregion

# region ornek_5
"""
bakiye = 5000
bankaKodu = 101
eftBankaKodu = 101
kesinti = 0
transfer = float(input("lütfen eft tutarını giriniz : "))
if bankaKodu != eftBankaKodu:
    kesinti = transfer*0.05
print(f"güncel bakiyeniz {bakiye - transfer - kesinti} TL.")
"""
# endregion

# region ornek_6
# 3 sayı girilecek en büyük ekrana yazılacak
"""
eb = 0
s = int(input("Lütfen Sayı Giriniz \t : "))
if s > eb:
    eb = s
s = int(input("Lütfen Sayı Giriniz \t : "))
if s > eb:
    eb = s
s = int(input("Lütfen Sayı Giriniz \t : "))
if s > eb:
    eb = s
print(f"Girilen Sayıların En Büyüğü {eb}")
"""
# endregion

# region ornek_7
"""
s1 = int(input("Lütfen 1. Sayı Giriniz \t : "))
s2 = int(input("Lütfen 2. Sayı Giriniz \t : "))
s3 = int(input("Lütfen 3. Sayı Giriniz \t : "))
ort = (s1+s2+s3) / 3
if ort >= 50:
    print(f"GEÇTİNİZ, ORTALAMANIZ {round(ort,2)}")
"""
# endregion


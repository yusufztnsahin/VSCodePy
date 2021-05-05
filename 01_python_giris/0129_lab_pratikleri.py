# region soru
"""
kilo = int(input("Lütfen kilonuzu giriniz:"))
boy = float(input("lütfen boyunuzu giriniz"))
v_k_e = kilo/(boy**2)
v_k_e = round(v_k_e, 3)
print(f"kilosu {kilo} ve boyu {boy} kişi için vucut kitle indeksiniz: {v_k_e}")
"""
# endregion

# region soru
"""
sayi1=int(input("Lütfen 1.Sayıyı giriniz :"))
sayi2=int(input("Lütfen 2.Sayıyı giriniz :"))
sayi3=int(input("Lütfen 3.Sayıyı giriniz :"))
ort=(sayi1+sayi2+sayi3)/3
print(f"{sayi1},{sayi2},{sayi3} sayılarının ortalaması {round(ort,2)}")
"""
# endregion

# region soru
"""
aKenari = int(input("Lütfen Üçgenin A Kenarı Açısını Giriniz: "))
bKenari = int(input("Lütfen Üçgenin B Kenarı Açısını Giriniz: "))
cKenari = (180-(aKenari+bKenari))
print(f"c kenarı {cKenari} derecedir")
"""
# endregion

# region soru
"""
aKenari = int(input("Lütfen A Kenarını Giriniz: "))
bKenari = int(input("Lütfen A Kenarını Giriniz: "))
alan = aKenari*bKenari
print(f"Dörtgenin Alnaı : {alan} metre karedir")
"""
# endregion

# region soru
"""
Kullanıcıdan x1,x2,y1,y2 değerleri alınır
- uzaklik =[ (x1-x2)karesi + (y1-y2)karesi ] karekök
- format : (x1,x2) ve (y1,y2) noktaları arasındaki uzaklık .. birimdir.
- virgülden 2 basamak olacaktır.
"""

"""
x1=int(input("x1 :"))
x2=int(input("x2 :"))
y1=int(input("y1 :"))
y2=int(input("y2 :"))
uzaklik=(((x1-x2)**2)+(y1-y2)**2)**.5
print(f"({x1},{x2}) ve ({y1},{y2}) noktaları arasındaki uzaklık {round(uzaklik,2)} birimdir.")
"""
# endregion

# region leylekUygulamasi
"""
print("
        leylek Uygulamasina Hoşgeldiniz!!!
        Ücreti → 0.69/dk
        ")   
s = int(input("sürüş için geçen süre (saat)\t: "))
d = int(input("sürüş için geçen süre (dakika)\t: "))
toplamDakika = s*60
toplamDakika += d
toplamTutar = toplamDakika*0.69
print(f"sürüş için geçen süre {s}:{d} dakika.")
print(f"sürüş için kredi kartından çekilen tutar {round(toplamTutar, 2)} TL.")
"""
# endregion

# region soru
"""
miktar=float(input("lütfen benzin endeksini girin\t:"))
yakit_tuketimi=float(input("lütfen yakıt tüketimini(100 km )  girin\t: "))
alinan_yol=int(input("aracın aldığı yolu girin \t:"))
toplam_tuketim=(yakit_tuketimi*alinan_yol*miktar)/100

print(toplam_tuketim)
"""
# endregion

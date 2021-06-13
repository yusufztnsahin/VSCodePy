"""
i, j = 0, 0
while i < 10:
    while j < 10:
        print(" * ", end="")
        j += 1
    i += 1
    j = 0
    print()
"""
"""
i, j = 0, 0
while i < 10:
    while j < 10:
        if i % 2 == 0:
            print(" * ", end="")
        else:
            print(" $ ", end="")
        j += 1
    i += 1
    j = 0
    print()
"""
"""
sayi = int(input("lütfen sayı giriniz\t:"))
i = 1
while i <= 5:
    print(f"{sayi } x {i} = {sayi*i}")
    i += 1
"""
"""
import random
uretilenSayi = random.randint(1, 99)   # [1-99] arası sayı üretir
print(uretilenSayi)
i = 0
enKucukFark=99999999999
while i<3:
    tahmin = int(input("lütfen [1-99] arası tahmininizi giriniz: \t"))    
    fark = uretilenSayi - tahmin
    if fark<0:
        fark *= -1
    if fark<enKucukFark:
        enKucukFark = fark
        enYakinTahmin = tahmin
    i += 1
print(enYakinTahmin)
"""
"""
i, j = 0, 10
while i<10:
    while j>0:
        print(" * ", end= "")
        j -= 1
    i += 1
    j = 10 -i
    print()
i, j = 0, 0
while i < 10:
    while j < i:
        print(" * ", end="")
        j += 1
    i += 1
    j = 0
    print()
"""
"""
i, j, n = 0, 0, 0
while i<4:
    while j<4:
        if n<i:
            print("   ", end="")
        else:
            print(" * ", end="")
        j +=1
        n +=1
    i +=1
    j = 0
    n = 0
    print()
"""
"""
i, j, n = 0, 0, 5
while i < 5:
    while j <=5:
        if n>0:
            print(".", end="")
        else:
            print(" *", end="")     
        j += 1
        n -=1
    i += 1
    n = 5- i
    j = 0
    print()
"""
"""
eb, count = 0, 0
while True:
    sayi = int(input("Lütfen bir sayi giriniz,çıkmak için -1 giriniz: "))
    if sayi == -1:
        break
    if sayi > eb:
        eb = sayi
    count += 1
if count:
    print(f"en büyük sayı {eb}")
else:
    print("hiç sayi girmediniz")
"""
"""
tekSayilarToplami, count = 0, 0
while True:
    sayi = int(input("Lütfen sayi giriniz çıkmak için -1 giriniz: "))
    if sayi == -1:
        break
    if sayi % 2 != 1:
        print("tek sayi giriniz!")
        continue
    tekSayilarToplami += sayi
    count += 1
print(f"Girilen tek sayılarrın ortalaması {tekSayilarToplami/count} olur")
"""

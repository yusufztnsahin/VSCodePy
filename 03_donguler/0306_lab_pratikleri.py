# region ornek_1
"""
1→  sonsuz döngü içinde kullanıcın girdiği sayıların
    tek olanlarının ortalamasını bulalım
2→  çift sayı girmeye çalıştığında ekrana uyarı verelim
3→  programı continue kulllanmalıyız
tekSayilarToplami = 0
while True:
    a = int(input("lütfen sayı giriniz, çıkmak için -1 giriniz: "))
    if a == -1:
        break
    if a % 2 != 1:
        print("lütfen tek sayı giriniz")
        continue
    tekSayilarToplami += a
print(f"listedeki tek sayıların toplamı {tekSayilarToplami}")
"""
# endregion
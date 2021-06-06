"""
sayiDizisi=list(range(10))
print(sayiDizisi)
"""
"""
Lütfen Sayı Giriniz:  40
1 2 4 5 8 10 20 40
"""
"""
sayi=int(input("lütfen sayı girniz"))
for i in range(1, sayi+1):
    if sayi%i==0:
        print(i,end= " ")
"""

#region odev
"""
    - Kullanıcının girdiği 2sayı arasındaki değerleri,
    her zaman küçükten büyüğe sıralayan for döngüsü yazın.
    1,10 -> 1,2,3,4,5,6,7,8,9
    10,1 -> 1,2,3,4,5,6,7,8,9
"""
"""
s1, s2 = int(input("1.sayıyı giriniz:\t")), int(input("2.sayıyı giriniz:\t"))
if s1>s2:
    s1,s2 = s2,s1
for i in range (s1,s2):
    print(i)
"""
#endregion


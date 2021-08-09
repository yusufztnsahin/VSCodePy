"""
kotuKelimeler = ["yuh", "tüh"]
yorum = "Bu laptop'u geçtiğimiz aylarda aldım. Aldığıma bin pişmanım. Satıcıya yuh sana diyorum."
kelimeler = [i.rstrip(".") for i in yorum.split(" ")]
for item in kotuKelimeler:
    if item in kelimeler:
        yorum = yorum.replace(item, "...")
print(yorum)
"""
meyveler = ["elma", "armut", "üzüm", "muz", "şeftali", "erik"]

print(meyveler[1:4])
print(meyveler[-2:])
print(meyveler)
print(meyveler[:])
print(meyveler[-1])
print(meyveler[1:5])
print(meyveler[1:5:1])
print(meyveler[1:5:2])
print(meyveler[1:15:2])
print(meyveler[:3])
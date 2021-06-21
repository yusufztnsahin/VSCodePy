kotuKelimeler = ["yuh", "tüh"]
yorum = "Bu laptop'u geçtiğimiz aylarda aldım. Aldığıma bin pişmanım. Satıcıya yuh sana diyorum."
kelimeler = [i.rstrip(".") for i in yorum.split(" ")]
for item in kotuKelimeler:
    if item in kelimeler:
        yorum = yorum.replace(item, "...")
print(yorum)

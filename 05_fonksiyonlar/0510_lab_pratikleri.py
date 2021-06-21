"""
carp(2, 3, 5)
carp(2, 3, 5, 6)
carp(2, 3, 5, 6, 15)
"""
"""
def carp(a, b, c, d=1, e=0):
    print(f"{a*b*c*d*e}")
carp(2, 3, 5, 6, 2)
"""

# region ornek_4
"""
1→ kayıtOl fonksiyonu yazılacak
2→ T.C. Kimlik, Ad, Email isimli üç adet argüman
3→ mail girilmez ise hata vermeyecek çıktıda '@' yazılacak
4→ ad girilmez ise hata vermeyecek çıktıda 'isimsiz' yazılacak
"""

# endregion
def kayitOl(tc, ad="isimsiz", email="@"):
    print(f"kayıt başarılı {tc} {ad} {email}")
kayitOl(24821842564)
kayitOl(24821842564, "yusuf")
kayitOl(24821842564, "yusuf", "email.com")
kayitOl(ad="yusuf",email="email.com",tc=24821842564)


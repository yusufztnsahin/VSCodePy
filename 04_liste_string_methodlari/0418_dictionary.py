# region dictionary
"""
1→ list
2→ tuple
3→ dictionary
1-) list özellikleri
→ tek bir değişken adında birden fazla eleman saklama
→ sıralı index özelliği
→ zero based’dir. İlk eleman [0], ikinci eleman [1]
→ duplicate eleman saklamaya izin vermesi
→ eleman değerlerinin değiştirilebilmesi
→ tanımlama anında, köşeli parantez [ ] kullanılması
2-) tuple özellikleri
→ tek bir değişken adında birden fazla eleman saklama
→ sıralı index özelliği. 
→ zero based’dir. İlk eleman [0], ikinci eleman [1]
→ duplicate eleman saklamaya izin vermesi
→ eleman değerlerinin değiştirilememesi
→ tanımlama anında, aç kapa parantez ( ) kullanılması
3-) dictionary özellikleri
→ tek bir değişken adında birden fazla eleman saklama
→ en önemli özelliği indisli değildir, sıralı değildir
→ key-value pair dediğimiz çiftler halinde tanımlanır
→ duplicate eleman saklamaya izin vermemesi
→ eleman değerlerinin değiştirilebilir olması
→ tanımlama anında, aç kapa süslü parantez { } kullanılması
"""


# endregion

# region dictionary_tanimlama_erisim
"""
programlaDilleri = {
    "programlamaDili": "python",
    "seviye": "yüksek",
    "interpreter": True,
    "versiyon": 3.94
}
print(programlaDilleri)
print(programlaDilleri["seviye"])
print(programlaDilleri.keys())
print(programlaDilleri.values())
print(programlaDilleri.items())
"""
# endregion

# region dictionary_duplicate
"""
programlaDilleri ={
    "programlamaDili" : "python",
    "seviye" : "yüksek",
    "interpterer" : True,
    "version": 3.91,
    "programlamaDili" : "c#",
}
print(programlaDilleri)
"""
# endregion

# region dictionary_loop
"""
programaDilleri ={
    "programlamaDili" : "python",
    "seviye" : "yüksek",
    "interpterer" : True,
    "version": 3.91
}
for key, value in programaDilleri.items():
    print(key, value)
"""

# endregion

# region ornek_1
"""
trEn ={
    "kitap" : "book",
    "geliştirici" : "developer",
    "korsan" : "hacker",
    "information": "bilgi"
}
for key, value in trEn.items():
    print(f"{key} ifadesinin ingilizcesi → {value}")
"""
"""
tring = {
    "öğrenci" : "student" ,
    "mühendis" : "engineer" ,
    "kalem" : "pencil"
}

for key,value in tring.items():
    print(f"{key} → {value}")

for i in tring.keys():
    print(f"{i}→ {tring[i]}")
"""
# endregion

# region ornek_2
"""
ipDetay = {
    "ip": {
        "query": "92.44.82.0",
        "status": "success",
        "continent": "Asia",
        "continentCode": "AS",
        "country": "Turkey",
        "countryCode": "TR",
        "region": "34",
        "regionName": "Istanbul",
        "city": "Istanbul",
        "district": "",
        "zip": "34110",
        "lat": 41.0205,
        "lon": 28.9753,
        "timezone": "Europe/Istanbul"
    },
    "dns": {
        "geo": "Turkey - Turkcell Internet"
    }
}
print(ipDetay["ip"]["lat"])
"""
# endregion

# region
"""
sirket = {
    "departman": {
        "yazılım": ["ali", "mehmet"],
        "muhasebe": ["inci", "elif"],
    },
    "calisanSayisi": 100,
    "ceo": "Ali Kemal",
    "telefonlar": {
        "istanbul": "021265656",
        "ankara": "031245656"
    },
    "sirketArabalari": ["i20", "renault megan", "ford focus"],
    "sirketArabalari2": {
        "i20": True,
        "renault megan": False,
        "ford focus": True
    }
}
print(sirket["calisanSayisi"])
print(sirket["ceo"])
print(sirket["departman"]["yazılım"])
print(sirket["departman"]["yazılım"][0])
print(sirket["sirketArabalari"][2])
print(sirket["sirketArabalari2"]["renault megan"])
"""
# endregion

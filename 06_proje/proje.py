# 1 → Kütüphaneleri import edelim
import json
import time
import requests
import urllib.parse
from datetime import datetime

# 2 → Customers API için gerekli URL girelim
urlCustomers = "https://northwind.netcore.io/customers?format=json"

# 3 → Customers API için GET request
rCustomers = requests.get("https://northwind.netcore.io/customers?format=json")

# 4 → if  case, bu kısımda her hangi bir kod değişikliği yapmayın lütfen
if not rCustomers.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rCustomers.status_code, rCustomers.text))


# 5 → Response içeriği print et referans amaçlı
#print(rCustomers.text)

# 6 → Response icerigi json data formatına encode et
jsonCustomers = json.loads(rCustomers.text)

# 7 → Orders API için gerekli URL'leri girelim
urlOrders = "https://northwind.netcore.io/orders?format=json"

# 8 → Orders API için GET request
rOrders = requests.get("https://northwind.netcore.io/orders?format=json")

# 9 → if  case, bu kısımda her hangi bir kod değişikliği yapmayın lütfen
if not rOrders.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rOrders.status_code, rOrders.text))

# 10 → Response içeriği print et referans amaçlı
#print(rOrders.text)

# 11 → response icerigi json data formatına encode et
jsonOrders = json.loads(rOrders.text)

# 12 → Mapquest API için gerekli URL'leri girelim
mainMapApiUrl = "https://www.mapquestapi.com/geocoding/v1/address?key=zYjDkhh9092lQJQy54YbnXCaldm4QMr7&location=istanbul"

# 13 → Mapquest Credential için; token, key... hazırlıkları yapalım
mapApiKey = "zYjDkhh9092lQJQy54YbnXCaldm4QMr7"


# 14 → UI manipulasyonu. Output anında 15 karakterden uzun metinler için manipulasyon yapalım
def metinKontrol(metin):
    if len(metin) > 15:
        return f"{metin[:15]}..."
    elif len(metin) <= 7:
        return f"{metin[:]}              "
        
    else:
        return f"{metin[:]}      "

# 15 → Müşterileri listeleyelim
def musteriListele():
    print("Müşteri Listesi")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CompanyName            |ContactName            |Address                |Country                |City                   |")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")

    for i in jsonCustomers["results"]:
        print(f"+{'-'*8}+{'-'*23}+{'-'*23}+{'-'*23}+{'-'*23}+{'-'*23}+\n|{i['id']}\t |{metinKontrol(i['companyName'])}\t |{metinKontrol(i['contactName'])}\t |{metinKontrol(i['address'])}\t |{metinKontrol(i['country'])}\t |{metinKontrol(i['city'])}")

    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")

# 16 → Müşterileri Id'ye göre arama yapalım
def musteriAra(musteriId):
    for i in jsonCustomers["results"]:
        if i['id']==musteriId:
            print(f"{musteriId} ID'li müşteri bulundu. Detay Listesi")
            print("==========================")
            print(f"{metinKontrol('Id')}\t\t:{i['id']}\n{metinKontrol('Firma Adı ')}\t\t:{i['companyName']}\n{metinKontrol('Müşteri Adı')}\t\t:{i['contactName']}\n{metinKontrol('İş Disiplini')}\t\t:{i['contactTitle']}\n{metinKontrol('Adres')}\t\t:{i['address']}\n{metinKontrol('Şehir')}\t\t:{i['city']}\n{metinKontrol('Posta Kodu')}\t\t:{i['postalCode']}\n{metinKontrol('Ülke')}\t\t:{i['country']}\n{metinKontrol('Telefon')}\t\t:{i['phone']}\n{metinKontrol('Fax')}\t\t:{i['fax']}")          
            break
    else:
        print(f"{musteriId} ID'li müşteri bulunamadı")
        
        
# 17 → Siparişleri listeleyelim    
def siparisListele():  
    print("Sipariş Listesi")
    print("+--------+-----------------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CustomerId             |OrderDate                      |ShipAddress            |ShipCity               |ShipCountry            |")
    print("+--------+-----------------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
    for i in jsonOrders["results"]:
        epochSaniye = int(i['order']["orderDate"][6:15])
        gunumuzZamani = time.ctime(epochSaniye)
        print(f"+{'-'*8}+{'-'*23}+{'-'*31}+{'-'*23}+{'-'*23}+{'-'*23}+\n|{i['order']['id']}\t |{metinKontrol(i['order']['customerId'])}\t |{(gunumuzZamani)}\t |{metinKontrol(i['order']['shipAddress'])}\t |{metinKontrol(i['order']['shipCity'])}\t |{metinKontrol(i['order']['shipCountry'])}")
    print("+--------+-----------------------+-------------------------------+-----------------------+-----------------------+-----------------------+")


# 18 → Sipariş Id'ye göre arama yapalım
def siparisAra(siparisId):
    for i in jsonOrders["results"]:
        if i['order']['id']==siparisId:
            epochSaniye = int(i['order']["orderDate"][6:15])
            gunumuzZamani = time.ctime(epochSaniye)
            print(f"{siparisId} ID'li sipariş bulundu. Detay Listesi")
            print("==========================")
            print(f"{metinKontrol('Sipariş Id')}\t\t:{i['order']['id']}\n{metinKontrol('Müşteri Id')}\t\t:{i['order']['customerId']}\n{metinKontrol('Firma Adı ')}\t\t:{i['order']['shipName']}\n{metinKontrol('Sipariş Tarihi')}\t\t:{gunumuzZamani}\n{metinKontrol('Adres')}\t\t:{i['order']['shipAddress']}\n{metinKontrol('Şehir')}\t\t:{i['order']['shipCity']}\n{metinKontrol('Ülke')}\t\t:{i['order']['shipCountry']}") 
            nereye = i['order']['shipCity']          
            cevap = input(f"Kargo Rotasını {nereye.upper()} Şehri İçin Görmek İster misiniz? [e/E] :")
            if cevap.lower()=="e":
                while True:                    
                    print(f"Varış Noktası {nereye} için Rota Hesaplanacak")
                    nereden = input("Nereden Çıkacak: ")
                    #<MapQuest API'yı Kullanarak Rota Belirlenecek>
                    break
            break
    else:
        print(f"{siparisId} ID'li sipariş bulunamadı")

# 19 → menu
while True:
    for i in range(5):
        print()
    secim = int(input("""
    Seçiminiz:
    [1]     → MÜŞTERİ LİSTELE
    [2]     → MÜŞTERİ ARA <MÜŞTERİ ID'E GÖRE>
    [3]     → SİPARİŞ LİSTELE
    [4]     → SİPARİŞ ARA <SİPARİŞ ID'E GÖRE>
    [5]     → ÇIK
    """))
    if secim==1:
        musteriListele()
    elif secim==2:
        musteri = input("Aranan Müşteri Id Giriniz      :")
        musteriAra(musteri.upper())
    elif secim==3:
        siparisListele()
    elif secim==4:
        siparis = int(input("Aranan Siparis Id Giriniz      :"))
        siparisAra(siparis)
    elif secim==5:
        break
    else:
        print("Hatalı Seçim!")
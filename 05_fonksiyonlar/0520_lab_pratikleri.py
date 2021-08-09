def kartBilgiVer(k):
    return f"{k['ad']} {k['soyad']} {k['bankaAdi']} {k['para']}"


def atmBilgiVer(a):
    return f"{a['ad']} {a['para']}"


def ayniMi(k, a):
    if k['bankaAdi'] == a['ad']:
        return True
    else:
        return False


def paraYatir(k, a, m):
    k['para'] += m
    a['para'] += m
    ceza(k,a,m)
        


def ceza(k, a, m):
    if not ayniMi(k, a):
        k['para'] -= m*0.02
        a['para'] += m*0.02


def paraCek(k, a, m):
    if a["para"] >= m:
        if k["para"] >= m:
            k['para'] -= m
            a['para'] -= m
            ceza(k,a,m)

        else:
            print(
                f"bakiyenizde {m} kadar miktar yok en fazla {k['para']} kadar para çekebilirsin")

    else:
        print(
            f"atm de {m} kadar miktar yok çekebileceğiniz max miktar {a['para']}")


kart = {
    "ad": "yusuf",
    "soyad": "şahin",
    "bankaAdi": "ziraat",
    "para": 1000
}

atm = {
    "ad": "halk",
    "para": 5000
}

#paraYatir(kart , atm , 1000)
paraCek(kart, atm, 500)
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))


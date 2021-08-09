def formatla(data):
    if len(data)>10:
        return data[:10]+"..."
    else:
        return data



def customers(kargs):
    print(f"{kargs['id']}\t{formatla(kargs['companyName'])}\t{formatla(kargs['contactName'])}\t{kargs['contactTitle']}\t{kargs['address']}")


customerALFKI = {
    "id" :"ALFKI",
    "companyName" : "Alfreds Futterkiste",
    "contactName" : "Maria Anders",
    "contactTitle" : "owner",
    "address" : "Obere Str. 57"
}

customerCACTU = {
    "id" :"CACTU",
    "companyName" : "Cactus Comidas para llevar",
    "contactName" : "Patricio Simpson",
    "contactTitle" : "Sales Agent",
    "address" : "Cerrito 333"
}

customers(customerALFKI)
customers(customerCACTU)

izlenmeSayisi = int(input("Lütfen izlenme sayısını giriniz: "))
if izlenmeSayisi < 1000:
    ek = izlenmeSayisi
elif izlenmeSayisi >= 1000 and izlenmeSayisi < 1000000:
    ek = (f"{izlenmeSayisi//1000} B")
elif izlenmeSayisi >= 1000000 and izlenmeSayisi < 1000000000:
    ek = (f"{round(izlenmeSayisi/1000000,1)} Mn")
elif izlenmeSayisi >= 1000000000:
    ek = (f"{round(izlenmeSayisi/1000000000,-1)} Ml")
print(ek)
import math

with open("in.txt","r",encoding="utf-8") as dosya:
    liste=[]
    sinif_sayisi = 10
    sinif_no = 0
    alt_siniflar=[]
    ust_siniflar=[]
    orta_degerler=[]
    frekanslar=[]
    goreli_frekanslar=[]

    for i in dosya.readlines():
        deger = i.split("\n")
        liste.append(float(deger[0]))
        liste.sort()
    print("Liste: {}".format(liste))

    siniflar = []
    for i in range(sinif_sayisi):
        siniflar.append(i+1)

    kucuk = min(liste)
    buyuk = max(liste)
    d = buyuk - kucuk
    c = round( d / sinif_sayisi , 2 )

    alt_deger = kucuk
    ust_deger = round((kucuk - 0.01 + c),2)
    orta_deger = round((alt_deger + ust_deger)/2,2)
    alt_siniflar.append(alt_deger)
    ust_siniflar.append(ust_deger)
    orta_degerler.append(orta_deger)

    for i in range(sinif_sayisi-1):
        alt_deger += c
        alt_siniflar.append(round(alt_deger , 2))
    print("Alt Siniflar: {}".format(alt_siniflar))

    for i in range(sinif_sayisi-1):
        ust_deger += c
        ust_siniflar.append(round(ust_deger,2))
    print("Ust Siniflar: {}".format(ust_siniflar))

    for i in range(sinif_sayisi-1):
        orta_deger += c
        orta_degerler.append(round(orta_deger,2))
    print("Orta Degerler: {}".format(orta_degerler))

    for i in range(sinif_sayisi):
        frekanslar.append(0)
    sayac = 0
    frekans_sayisi = 0
    for i in liste:
        if(i <= ust_siniflar[sayac] and i>=alt_siniflar[sayac]):
            frekanslar[sayac] += 1
        else:
            sayac = sayac + 1
            frekanslar[sayac] += 1
    print("Frekanslar: {}".format(frekanslar))

    toplam_frekans=0
    for i in frekanslar:
        toplam_frekans +=i

    for i in range(sinif_sayisi):
        goreli_frekanslar.append(round(frekanslar[i]/toplam_frekans, 2))
    print("Goreli Frekanslar: {}".format(goreli_frekanslar))

    toplam = 0
    for i in range(sinif_sayisi):
        toplam += (orta_degerler[i] * frekanslar[i])
        ortalama = round((toplam / toplam_frekans),2)

    ara_toplam = 0
    for i in range(len(liste)):
        ara_toplam += (liste[i] - ortalama) ** 2
    varyans = ara_toplam / len(liste)
    stardart_sapma = math.sqrt(varyans)


    max_frekans = max(frekanslar)
    for i in range(len(frekanslar)):
        if (frekanslar[i] == max_frekans):
            mod_sinifi = i
            break
    d1 = frekanslar[mod_sinifi] - frekanslar[mod_sinifi - 1]
    d2 = frekanslar[mod_sinifi] - frekanslar[mod_sinifi + 1]
    mod = alt_siniflar[mod_sinifi] + (d1 / (d1 + d2)) * c


    medyan_sinifi = 0
    for i in range(len(frekanslar)):
        medyan_sinifi+=frekanslar[i]
        if(medyan_sinifi >= toplam_frekans/2):
            break
    medyan_sinifi = i

    onceki_siniflar = 0
    for i in range(medyan_sinifi):
        onceki_siniflar += frekanslar[i]
    medyan = alt_siniflar[medyan_sinifi] + (((toplam_frekans/2) - onceki_siniflar)/frekanslar[medyan_sinifi]) * c


    print("Degisim Araligi: {}".format(d))
    print("Sinif Araligi: {}".format(c))
    print("Ortalama: {}".format(ortalama))
    print("Mod: {}".format(mod))
    print("Medyan: {}".format(medyan))
    print("Varyans: {}".format(varyans))
    print("Standart Sapma: {}".format(stardart_sapma))

with open("out.txt","a",encoding="utf-8") as dosya:
    dosya.write("\n")
    dosya.write("Siniflar\tAlt Deger \t Ust Deger \t Orta_deger \t Frekans \t Goreli Frekans \n")
    for i in range(sinif_sayisi):
        dosya.write("{:<6}".format(str(siniflar[i])) + "\t" + "\t"
        +"{:<8}".format(str(alt_siniflar[i])) + "\t" + "\t"
        + "{:<7}".format(str(ust_siniflar[i])) + "\t" + "\t"
        + "{:<8}".format(str(orta_degerler[i])) + "\t" + "\t"
        + "{:<7}".format(str(frekanslar[i])) + "\t" + "\t"
        + "{:<8}".format(str(goreli_frekanslar[i]) )+"\t" +"\t" +"\n")
    dosya.write("\n")
    dosya.write("Ortalama       = {}".format(ortalama) + "\n")
    dosya.write("Mod            = {}".format(mod) + "\n")
    dosya.write("Medyan         = {}".format(medyan) + "\n")
    dosya.write("Varyans        = {}".format(varyans) + "\n")
    dosya.write("Standart Sapma = {}".format(stardart_sapma) + "\n")


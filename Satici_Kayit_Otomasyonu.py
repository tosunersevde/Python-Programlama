# 20010011044 / Sevde Nur TOSUNER

import random

def Menu():
    print("-----------------------------------------")
    print("     Ev Esyasi Online Satis Platformu    ")
    print("-----------------------------------------")
    print( "[1]-Kayit Ekleme")
    print( "[2]-Kayit Silme")
    print("[3]-Kayit Guncelleme")
    print("[4]-Kayit Listeleme")
    print("[5]-Kayit Numara Aramasi")
    print("[6]-Kayit Ad Aramasi")
    print("[0]-Cikis")

    secim = input("Yapmak Istediginiz Islemi Seciniz: ")
    return secim

def Satici_Kayit_Ekleme():

    with open("SaticiKayitlari.txt", "a", encoding="utf-8") as dosya:
        satici_sayi = int(input("Satici Sayisini Giriniz: "))
        saticilar = {}
        satici_no = random.randint(100,500)

        for i in range(satici_sayi):
            satici_bilgi = {}
            satici_ad = input("{}.Saticinin Adini Giriniz: ".format(i + 1))
            satici_bilgi["Saticinin Adi:"] = satici_ad
            satici_soyad = input("{}.Saticinin Soyadini Giriniz: ".format(i + 1))
            satici_bilgi["Saticinin Soyadi:"] = satici_soyad
            bulundugu_sehir = input("{}.Saticinin Bulundugu Sehri Giriniz: ".format(i + 1))
            satici_bilgi["Sehri:"] = bulundugu_sehir
            satilan_esya = input("{}.Saticin Sattigi Esyanin Turunu Giriniz: ".format(i + 1))
            satici_bilgi["Turu:"] = satilan_esya
            esya_durum = input("{}.Saticinin Sattigi Esyanin Durumunu Giriniz(Hasarli-Saglam): ".format(i+1))
            satici_bilgi["Satilan Urunun Turu:"] = esya_durum
            esya_fiyat = input("{}.Saticinin Sattigi Esyanin Fiyatini Giriniz: ".format(i+1))
            satici_bilgi["Satilan Urunun Fiyati:"] = esya_fiyat

            saticilar[satici_no + i] = satici_bilgi

        for i in saticilar.keys():
            dosya.write(str(i) + " ") # Bosluk ekleyebilmek icin str'ye donusturuldu.
            for j in saticilar[i].values():
                dosya.write(j + " ")
            dosya.write("\n")

    print("Kayit Eklendi!")

def Satici_Kayit_Silme():

    with open("SaticiKayitlari.txt", "r", encoding="utf-8") as dosya:
        saticilar = {}
        numara = input("Silinecek Saticinin Numarasini Giriniz: ")
        kontrol = None

        for i in dosya.readlines():
            deger = i.split(" ")

            anahtar, deger = deger[0], deger[1:7] # Sonuncu karakter "\n" oldugu icin 7'ye kadar olan degerler alindi.
            saticilar[anahtar] = deger

            if numara == anahtar:
                kontrol = True
                saticilar.pop(anahtar)

        if kontrol:
            with open("SaticiKayitlari.txt", "w", encoding="utf-8") as d:
                for i in saticilar.keys():
                    d.write(i + " ")
                    for j in range(len(saticilar[i])):
                        d.write(saticilar[i][j] + " ")
                    d.write("\n")
            print("Silme Islemi Gerceklesti!")
        else:
            print("Aradiginiz Urun Bulunamamıstır!")

def Satici_Kayit_Guncelleme():

    numara = input("Guncellemek Istedginiz Saticinin Numarasini Giriniz: ")

    def Kayit_Silme():
        with open("SaticiKayitlari.txt", "r", encoding="utf-8") as dosya:
            saticilar = {}
            kontrol = None

            for i in dosya.readlines():
                deger = i.split(" ")

                anahtar, deger = deger[0], deger[1:7]
                saticilar[anahtar] = deger

                if numara == anahtar:
                    kontrol = True
                    saticilar.pop(anahtar)

            if kontrol:
                with open("SaticiKayitlari.txt", "w", encoding="utf-8") as d:
                    for i in saticilar.keys():
                        d.write(i + " ")
                        for j in range(len(saticilar[i])):
                            d.write(saticilar[i][j] + " ")
                        d.write("\n")
            else:
                print("Aradiginiz Urun Bulunamadi!")

    Kayit_Silme()

    def Kayit_Ekleme():
        with open("SaticiKayitlari.txt", "a", encoding="utf-8") as dosya:
            saticilar = {}
            satici_no = numara

            satici_bilgi = {}
            satici_ad = input("Saticinin Yeni Adini Giriniz: ")
            satici_bilgi["Saticinin Adi:"] = satici_ad
            satici_soyad = input("Saticinin Yeni Soyadini Giriniz: ")
            satici_bilgi["Saticinin Soyadi:"] = satici_soyad
            bulundugu_sehir = input("Saticinin Bulundugu Yeni Sehri Giriniz: ")
            satici_bilgi["Sehri:"] = bulundugu_sehir
            satilan_esya = input("Saticin Sattigi Esyanin Yeni Turunu Giriniz: ")
            satici_bilgi["Turu:"] = satilan_esya
            esya_durum = input("Saticinin Sattigi Esyanin Yeni Durumunu Giriniz(Hasarli-Saglam): ")
            satici_bilgi["Satilan Urunun Turu:"] = esya_durum
            esya_fiyat = input("Saticinin Sattigi Esyanin Yeni Fiyatini Giriniz: ")
            satici_bilgi["Satilan Urunun Fiyati:"] = esya_fiyat

            saticilar[satici_no] = satici_bilgi

            for i in saticilar.keys():
                dosya.write(str(i) + " ")
                for j in saticilar[i].values():
                    dosya.write(j + " ")
                dosya.write("\n")

    Kayit_Ekleme()

    print("Guncelleme Islemi Gerceklesti!")

def Kayitlari_Listeleme():

    with open("SaticiKayitlari.txt", "r", encoding="utf-8") as dosya:
        saticilar = {}

        for i in dosya.readlines():
            deger = i.split(" ")

            anahtar, deger = deger[0], deger[1:7]
            saticilar[anahtar] = deger

        for i in saticilar.keys():
            print(i + " ")
            for j in range(len(saticilar[i])):
                print(saticilar[i][j] + " ")
            print("\n")

def Kayit_Numara_Aramasi():

    with open("SaticiKayitlari.txt", "r", encoding="utf-8") as dosya:
        saticilar = {}
        kontrol = None
        numara = input("Aranan Saticinin Numarasini Giriniz: ")

        for i in dosya.readlines():
            deger = i.split(" ")

            anahtar, deger = deger[0], deger[1:7]
            saticilar[anahtar] = deger

            if numara == anahtar:
                kontrol = True
                break

        if kontrol:
            for i in range(len(saticilar[anahtar])):
                print(saticilar[anahtar][i] + " ")
            print("\n")
        else:
            print("Aradiginiz Satici Bulunamadi!")

def Kayit_Ad_Aramasi():

    with open("SaticiKayitlari.txt", "r", encoding="utf-8") as dosya:
        saticilar = {}
        kontrol = None
        ad = input("Aranan Saticinin Adini Giriniz: ")

        for i in dosya.readlines():
            deger = i.split(" ")

            anahtar, deger = deger[0], deger[1:7]
            saticilar[anahtar] = deger

            if ad == saticilar[anahtar][0]: # Ilk deger isim degeri oldugu icin [0]. deger alinmistir.
                kontrol = True
                break

        if kontrol:
            for _ in saticilar.keys():
                for i in range(len(saticilar[anahtar])):
                    print(saticilar[anahtar][i] + " ")
                print("\n")
                break
        else:
            print("Aradiginiz Satici Bulunamadi!")

while True:

    secim_1 = Menu()

    if secim_1 == "1":
        Satici_Kayit_Ekleme()
    elif secim_1 == "2":
        Satici_Kayit_Silme()
    elif secim_1 == "3":
        Satici_Kayit_Guncelleme()
    elif secim_1 == "4":
        Kayitlari_Listeleme()
    elif secim_1 == "5":
        Kayit_Numara_Aramasi()
    elif secim_1 == "6":
        Kayit_Ad_Aramasi()
    elif secim_1 == "0":
        break
    else:
        print("Yanlis Secim Yaptiniz!")
        secim_2 = input("Devam Etmek Icın Herhangi Bir Sayi Tuslayınız: ")
        continue

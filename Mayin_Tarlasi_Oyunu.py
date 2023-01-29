import random
while True:
    mayin_tarlasi=[]
    while True:
        tarla_alan=int(input("Mayin Tarlasi Alanini Giriniz(10 ve 10'dan Buyuk Girilmelidir! ): "))
        if tarla_alan<10:
            print("Lutfen Tarlanin Alanini 10'dan Buyuk Giriniz: ")
        else:
            break

    puan=0

    for i in range(tarla_alan):
        mayin_tarlasi.append(["?"]*tarla_alan)

    def tarla_yazdirma(mayin_tarlasi):
        for satir in mayin_tarlasi:
            print(" ".join(satir))

    mayin_sayisi =int(tarla_alan * tarla_alan * 0.3)
    mayinlar=[]

    def satir_olusturma():
        for i in range(mayin_sayisi):
            rastgele_satir=random.randint(0,tarla_alan-1)
            return rastgele_satir

    def sutun_olusturma():
        for i in range(mayin_sayisi):
            rastgele_sutun=random.randint(0,tarla_alan-1)
            return rastgele_sutun

    for i in range(mayin_sayisi):
        mayinlar.append([satir_olusturma(), sutun_olusturma()])


    print("Mayin Tarlasi Oyununa Hosgeldiniz!\n")
    print("Lutfen Oyunu Oynamak Istediginiz Modu Seciniz! \n1-> Gizli Mod, 2-> Acik Mod")
    secim_1 = input("Seciminizi Giriniz: ")


    if secim_1=="1":
        for i in range(mayin_sayisi):
            if mayinlar.count(mayinlar[i])>1:
                mayinlar.remove(mayinlar[i])
                mayinlar.append([satir_olusturma(), sutun_olusturma()])
        tarla_yazdirma(mayin_tarlasi)
        while True:
            print(mayinlar)
            print("Mayinin Bulundugu Tahmini Konumunuzu Giriniz!")
            satir = int(input("Satir Giriniz: "))
            sutun = int(input("Sutun Giriniz: "))

            tahmin = [satir,sutun]

            etraftaki_mayin = 0
            if tahmin[0]<0 or tahmin[1]<0 or tahmin[0]>tarla_alan or tahmin[1]>tarla_alan:
                print("Tarla Sinirlari Disinda Tahminde Bulundunuz!")

            else:
                if [tahmin[0],tahmin[1]] in mayinlar:
                    print("Maalesef Kaybettiniz! Puaniniz: {}".format(puan))
                    for i in range(mayin_sayisi):
                        mayin_tarlasi[mayinlar[i][0]][mayinlar[i][1]] = "X"
                    tarla_yazdirma(mayin_tarlasi)
                    break
                else:
                    if mayin_tarlasi[tahmin[0]][tahmin[1]] == "?":
                        puan+=1
                        # SAĞ ALT
                        if tahmin[0] + 1 < tarla_alan and tahmin[1] + 1 < tarla_alan and [tahmin[0] + 1, tahmin[1] + 1] in mayinlar:
                            etraftaki_mayin += 1
                        # ALT
                        if tahmin[0] + 1 < tarla_alan and [tahmin[0] + 1, tahmin[1]] in mayinlar:
                            etraftaki_mayin += 1
                        # SOL ALT
                        if tahmin[0] + 1 < tarla_alan and tahmin[1] - 1 >= 0 and [tahmin[0] + 1, tahmin[1] - 1] in mayinlar:
                            etraftaki_mayin += 1
                        # SAĞ
                        if tahmin[1] + 1 < tarla_alan and [tahmin[0], tahmin[1] + 1] in mayinlar:
                            etraftaki_mayin += 1
                        # SOL
                        if tahmin[0] < tarla_alan and tahmin[1] - 1 >= 0 and [tahmin[0] + 1, tahmin[1] - 1] in mayinlar:
                            etraftaki_mayin += 1
                        # SAĞ ÜST
                        if tahmin[0] - 1 >= 0 and tahmin[1] + 1 < tarla_alan and [tahmin[0] - 1, tahmin[1] + 1] in mayinlar:
                            etraftaki_mayin += 1
                        # ÜST
                        if tahmin[0] - 1 >= 0 and [tahmin[0] - 1, tahmin[1]] in mayinlar:
                            etraftaki_mayin += 1
                        # SOL ÜST
                        if tahmin[0] - 1 >= 0 and tahmin[1] - 1 >= 0 and [tahmin[0] - 1, tahmin[1] - 1] in mayinlar:
                            etraftaki_mayin += 1

                        mayin_tarlasi[tahmin[0]][tahmin[1]] = str(etraftaki_mayin)
                        tarla_yazdirma(mayin_tarlasi)
                        continue
                    else:
                        print("Bu Tahmin Daha Once Yapilmistir!")

            if puan==int(tarla_alan * tarla_alan * 0.7):
                print("Tebrikler Oyunu Kazandiniz! Puaniniz: ".format(puan))
                break


    elif secim_1=="2":
        for i in range(mayin_sayisi):
            if mayinlar.count(mayinlar[i])>1:
                mayinlar.remove(mayinlar[i])
                mayinlar.append([satir_olusturma(), sutun_olusturma()])
            mayin_tarlasi[mayinlar[i][0]][mayinlar[i][1]] = "X"
        tarla_yazdirma(mayin_tarlasi)
        while True:
            print(mayinlar)
            satir= int(input("Satir Giriniz: "))
            sutun= int(input("Sutun Giriniz: "))

            tahmin = [satir, sutun]

            etraftaki_mayinn = 0
            if tahmin[0]<0 or tahmin[1]<0 or tahmin[0]>tarla_alan or tahmin[1]>tarla_alan:
                print("Tarla Sinirlari Disinda Tahminde Bulundunuz!")
            else:
                if mayin_tarlasi[tahmin[0]][tahmin[1]] == "X":
                    print("Maalesef Kaybettiniz! Puanininiz: {}".format(puan))
                    break

                else:
                    if mayin_tarlasi[tahmin[0]][tahmin[1]] == "?":
                        puan += 1
                        # SAĞ ALT
                        if tahmin[0] + 1 < tarla_alan and tahmin[1] + 1 < tarla_alan and [tahmin[0] + 1, tahmin[1] + 1] in mayinlar:
                            etraftaki_mayinn += 1
                        # ALT
                        if tahmin[0] + 1 < tarla_alan and [tahmin[0] + 1, tahmin[1]] in mayinlar:
                            etraftaki_mayinn += 1
                        # SOL ALT
                        if tahmin[0] + 1 < tarla_alan and tahmin[1] - 1 >= 0 and [tahmin[0] + 1, tahmin[1] - 1] in mayinlar:
                            etraftaki_mayinn += 1
                        # SAĞ
                        if tahmin[1] + 1 < tarla_alan and [tahmin[0], tahmin[1] + 1] in mayinlar:
                            etraftaki_mayinn += 1
                        # SOL
                        if tahmin[0] < tarla_alan and tahmin[1] - 1 >= 0 and [tahmin[0] + 1, tahmin[1] - 1] in mayinlar:
                            etraftaki_mayinn += 1
                        # SAĞ ÜST
                        if tahmin[0] - 1 >= 0 and tahmin[1] + 1 < tarla_alan and [tahmin[0] - 1, tahmin[1] + 1] in mayinlar:
                            etraftaki_mayinn += 1
                        # ÜST
                        if tahmin[0] - 1 >= 0 and [tahmin[0] - 1, tahmin[1]] in mayinlar:
                            etraftaki_mayinn += 1
                        # SOL ÜST
                        if tahmin[0] - 1 >= 0 and tahmin[1] - 1 >= 0 and [tahmin[0] - 1, tahmin[1] - 1] in mayinlar:
                            etraftaki_mayinn += 1

                        mayin_tarlasi[tahmin[0]][tahmin[1]] = str(etraftaki_mayinn)
                        tarla_yazdirma(mayin_tarlasi)
                        continue
                    else:
                        print("Bu Tahmin daha Once Yapilmistir!")

            if puan==int(tarla_alan * tarla_alan * 0.7):
                print("Tebrikler Oyunu Kazandiniz! Puaniniz: ".format(puan))
                break

    print("Oyun Bitti! Tekrar Oynamak Icin -> 1'i Seciniz! Cikis icin -> 2'yi Seciniz!")
    secim_2 = input("Seciminizi Giriniz: ")

    if secim_2=="2":
        break
    elif secim_2=="1":
        continue
    else:
        print("Yanlis Secim Yaptiniz!")


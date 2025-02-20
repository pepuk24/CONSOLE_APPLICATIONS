def kilomenu():
    
    
    print("╔═════════════════════════════════╗")
    print("║     Sağlık(Kilo Hesaplayıcı)    ║")
    print("║                                 ║")
    print("║  1- Vücut Kitle İndeksi'ne      ║")
    print("║     Göre İdeal Kilo Hesaplama   ║")
    print("║  2- Broca Formülü İle           ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║  3- Erkekler İçin               ║")
    print("║     Robinson Formülü İle        ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║ 4- Kadınlar İçin                ║")
    print("║     Robinson Formülü İle        ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║ 5- Kilo Durumu Değerlendirme    ║")
    print("║ 6- İdeal Kilo Hesaplayarak      ║")
    print("║     Kilo Durumu Değerlendirmesi ║")
    print("║ 7- Ana Menü                     ║")
    print("║           Seçiminiz nedir?      ║")
    print("║                                 ║")
    print("╚═════════════════════════════════╝")
    print()

    secim = input("Lütfen seçiminizin başındaki sayıyı yazınız:")

    if secim == "1":
        kilo = int(input("Lütfen kilonuzu giriniz (KG):"))
        boy = int(input("Lütfen boyunuzu giriniz (CM):"))
        boy_m = boy / 100
        vki = kilo / (boy_m ** 2)
        ik = 22 * (boy_m ** 2)
        print(f"Vücut kitle endeksiniz {vki:.2f} kg/m2, ideal kilonuz {int(ik)} kg'dır.")
        kilomenu()

    elif secim == "2":
        boy = int(input("Lütfen boyunuzu giriniz (CM):"))
        ik2 = (boy - 100) - ((boy - 150) / 4)
        print(f"Broca formülüne göre ideal kilonuz: {int(ik2)} kg")
        kilomenu()

    elif secim == "3":
        boy = int(input("Lütfen boyunuzu giriniz (CM):"))
        ik3 = 52 + 1.9 * ((boy - 152.4) / 2.54)
        print(f"Erkekler için Robinson formülüne göre ideal kilonuz: {int(ik3)} kg")
        kilomenu()

    elif secim == "4":
        boy = int(input("Lütfen boyunuzu giriniz (CM):"))
        ik4 = 49 + 1.7 * ((boy - 152.4) / 2.54)
        print(f"Kadınlar için Robinson formülüne göre ideal kilonuz: {int(ik4)} kg")
        kilomenu()

    elif secim == "5":
        kilo = int(input("Lütfen kilonuzu giriniz (KG):"))
        boy = int(input("Lütfen boyunuzu giriniz (CM):"))
        boy_m = boy / 100
        vki = kilo / (boy_m ** 2)
        if vki < 18.5:
            print("Zayıf")
        elif 18.5 <= vki < 24.9:
            print("Normal kilolu")
        elif 25 <= vki < 29.9:
            print("Fazla kilolu")
        else:
            print("Obez")
        kilomenu()

    elif secim == "6":
        kilo = int(input("Lütfen kilonuzu giriniz (KG):"))
        boy = int(input("Lütfen boyunuzu giriniz (CM):"))
        boy_m = boy / 100
        vki = kilo / (boy_m ** 2)
        ik = 22 * (boy_m ** 2)
        print(f"Vücut kitle endeksiniz {vki:.2f} kg/m2, ideal kilonuz {int(ik)} kg'dır.")
        if kilo > ik:
            print(f"İdeal kilonuzdan {int(kilo - ik)} kg fazlanız var.")
        elif kilo < ik:
            print(f"İdeal kilonuzdan {int(ik - kilo)} kg eksiksiniz.")
        else:
            print("İdeal kilonuzdasınız.")
        kilomenu()

    elif secim == "7":
        print("Ana Menü'ye dönülüyor.")
        return

    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        kilomenu()

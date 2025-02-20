def mesafemenu():
    print("\033[34m                                                                      ")
    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║")
    print("                               ║             MESAFE ÇEVİRİCİ                  ║")
    print("                               ║                                              ║")
    print("                               ╚══════════════════════════════════════════════╝")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║") 
    print("                               ║                                              ║")
    print("                               ║         1-METRE ==> KİLOMETRE                ║")
    print("                               ║         2-KM    ==> METRE                    ║")
    print("                               ║         3-METRE ==> İNÇ                      ║")
    print("                               ║         4-İNÇ   ==> METRE                    ║")                             
    print("                               ║         5-KM    ==> MİL                      ║")
    print("                               ║         6-MİL   ==> KİLOMETRE                ║")
    print("                               ║         7-FEET  ==> KİLOMETRE                ║") 
    print("                               ║         8-KM    ==> FEET                     ║") 
    print("                               ║         9-YARD  ==> KİLOMETRE                ║") 
    print("                               ║         10-KM   ==> YARD                     ║")
    print("                               ║                                              ║")
    print("                               ║             SEÇİMİNİ YAP!!                   ║")
    print("                               ╚══════════════════════════════════════════════╝")

    secim = input("Lütfen seçiminizi yapınız: ")

    if secim == "1":
        metre=float(input("Metreyi giriniz\t:"))
        sonuc=metre/1000
        print(f"{metre} metre= {sonuc} kilometre")
    elif secim=="2":
        km=float(input("Km'yi giriniz\t:"))
        sonuc=km*1000
        print(f"{km} kilometre {sonuc} metre eder...")

    elif secim=="3":
        metre=float(input("Metre'yi girirniz\t:"))
        sonuc=metre*39.3701
        print(f"{metre} metre {sonuc} inç eder...")

    elif secim=="4":
        inç=float(input("İnç yazınız\t:"))
        sonuc=inç/1000
        print(f"{inç} inç {sonuc} metre eder...")

    elif secim=="5":
        km=float(input("Lutfen km yazınız\t:"))
        sonuc=km*0.621371
        print(f"{km} km {sonuc} Mil eder...")
    elif secim=="6":
        mil=float(input("Lutfen mil giriniz\t:"))
        sonuc=mil*1.60934
        print(f"{mil}mil {sonuc} km eder...")

    elif secim == "7":
        feet = float(input("Lütfen feet giriniz\t:"))
        sonuc = feet * 0.0003048
        print(f"{feet} feet = {sonuc} kilometre")
    elif secim == "8":
        km = float(input("Lütfen km giriniz\t:"))
        sonuc = km * 3280.84
        print(f"{km} km = {sonuc} feet")
    elif secim == "9":
        yard = float(input("Lütfen yard giriniz\t:"))
        sonuc = yard * 0.0009144
        print(f"{yard} yard = {sonuc} kilometre")
    elif secim == "10":
        km = float(input("Lütfen km giriniz\t:"))
        sonuc = km * 1093.61
        print(f"{km} km = {sonuc} yard")
    else:
        print("Geçersiz seçim yaptınız. Lütfen tekrar deneyin.")

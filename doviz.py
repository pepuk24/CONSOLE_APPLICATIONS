def dovizmenu():
    while True:
        print("\033[34m")  # Mavi renk
        print("                               ╔══════════════════════════════════════════════╗")
        print("                               ║                                              ║")
        print("                               ║             DÖVİZ BÜROSU                     ║")
        print("                               ║ Kur fiyatları ŞUBAT-2025'te güncellenmiştir.  ║")
        print("                               ╚══════════════════════════════════════════════╝")

        print("                               ╔══════════════════════════════════════════════╗")
        print("                               ║                                              ║") 
        print("                               ║         1 TL ==> $                           ║")
        print("                               ║         2 $  ==> TL                          ║")                             
        print("                               ║         3 TL ==> £                           ║")
        print("                               ║         4 £  ==> TL                          ║") 
        print("                               ║         5 Çıkış                              ║")
        print("                               ║                                              ║")
        print("                               ║          SEÇİMİNİ YAP!!                      ║")
        print("                               ╚══════════════════════════════════════════════╝")

        secim = input("Lütfen uygulama seçimini yapınız: ")  

        # Döviz kurları (Sabit değerler)
        dolar_kuru = 40  # 1$ = 40 TL
        sterlin_kuru = 50  # 1£ = 50 TL

        if secim == "1":
            TL = float(input("Lütfen TL miktarını giriniz: "))
            deger = TL / dolar_kuru
            print(f"{TL:.2f} TL = {deger:.2f} $ eder.\n")

        elif secim == "2":
            USD = float(input("Lütfen USD miktarını giriniz: "))
            deger = USD * dolar_kuru
            print(f"{USD:.2f} $ = {deger:.2f} TL eder.\n")

        elif secim == "3":
            TL = float(input("Lütfen TL miktarını giriniz: "))
            deger = TL / sterlin_kuru
            print(f"{TL:.2f} TL = {deger:.2f} £ eder.\n")

        elif secim == "4":
            GBP = float(input("Lütfen GBP miktarını giriniz: "))
            deger = GBP * sterlin_kuru
            print(f"{GBP:.2f} £ = {deger:.2f} TL eder.\n")

        elif secim == "5":
            print("Programdan çıkılıyor... Görüşmek üzere!")
            break

        else:
            print("❌ Geçersiz seçim! Lütfen 1-5 arasında bir değer girin.\n")

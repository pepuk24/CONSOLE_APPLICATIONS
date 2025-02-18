def dovizmenu():

 
    print("\033[34m                                                                      ")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║")
    print("                               ║             DÖVİZ BÜROSU                     ║")
    print("                               ║ Kur fiyatları ŞUBAT-2025' güncellenmiştir.   ║")
    print("                               ╚══════════════════════════════════════════════╝")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║") 
    print("                               ║                                              ║")
    print("                               ║         1 TL==>$                             ║")
    print("                               ║                                              ║")
    print("                               ║         2 $==>TL                             ║")                             
    print("                               ║                                              ║")
    print("                               ║         3 TL==>£                             ║")
    print("                               ║                                              ║") 
    print("                               ║         4 £==>TL                             ║") 
    print("                               ║                                              ║") 
    print("                               ║         5-Çıkış                              ║")
    print("                               ║                                              ║")
    print("                               ║          SEÇİMİNİ YAP!!                      ║")
    print("                               ╚══════════════════════════════════════════════╝")

    secim = input("Lütfen uygulama seçimini yapınız: ")  

    if secim=="1":
        TL= int(input("Lutfen bir deger giriniz\t:"))
        deger=TL/40
        print (f"{TL } TL {deger} $ eder...")



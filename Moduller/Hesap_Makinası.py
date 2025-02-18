def hesapmenu():
    print("\033[34m                                                                      ")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║")
    print("                               ║              HESAP MAKİNASI                  ║")
    print("                               ║                                              ║")
    print("                               ╚══════════════════════════════════════════════╝")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║") 
    print("                               ║                                              ║")
    print("                               ║         1-TOPLAMA                            ║")
    print("                               ║                                              ║")
    print("                               ║         2-ÇARPMA                             ║")                             
    print("                               ║                                              ║")
    print("                               ║         3-ÇIKARTMA                           ║")
    print("                               ║                                              ║") 
    print("                               ║         4-BÖLME                              ║") 
    print("                               ║                                              ║") 
    print("                               ║         5-ÇIKIŞ                              ║")
    print("                               ║                                              ║")
    print("                               ║          SEÇİMİNİ YAP!!                      ║")
    print("                               ╚══════════════════════════════════════════════╝")

secim = input("Seçim yapınız: ")

def topla(a, b):
    return a + b

def çarp(a, b):
    return a * b

def çıkart(a, b):
    return a - b

def böl(a, b):
    if b == 0:
        return "Hata! Bir sayı 0'a bölünemez..."
    return a / b

if secim in ["1", "2", "3", "4"]:
    s1 = int(input("1.sayıyı giriniz\t:"))
    s2 = int(input("2.sayıyı giriniz\t:"))

    if secim == "1":
        sonuc = topla(s1, s2)
        print(f"Sonuç\t: {sonuc}")
    elif secim == "2":
        sonuc = çarp(s1, s2)
        print(f"Sonuç\t: {sonuc}")
    elif secim == "3":
        sonuc = çıkart(s1, s2)
        print(f"Sonuç\t: {sonuc}")
    elif secim == "4":
        sonuc = böl(s1, s2)
        print(f"Sonuç\t: {sonuc}")

    input("Ana menüye dönmek için Enter'a basın...")  # Sonucu göstermesi için bekletme

elif secim == "5":
    print("Çıkış yapılıyor...")
    exit()
else:
    print("Hata: Geçersiz giriş yaptınız, lütfen 1-5 arasında bir rakam girin.")
   

hesapmenu()
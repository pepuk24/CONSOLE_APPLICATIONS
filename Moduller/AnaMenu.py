import mesafe_birim
import oyunlar
import takvim
import doviz

def anamenu():
    '''
anamenu 
    '''
    print("\033[34m                                                                      ")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║")
    print("                               ║              UYGULAMALAR                     ║")
    print("                               ║                                              ║")
    print("                               ╚══════════════════════════════════════════════╝")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║") 
    print("                               ║                                              ║")
    print("                               ║         1-MESAFE BİRİM ÖLÇÜMÜ                ║")
    print("                               ║                                              ║")
    print("                               ║         2-OYUNLAR                            ║")                             
    print("                               ║                                              ║")
    print("                               ║         3-TAKVİM                             ║")
    print("                               ║                                              ║") 
    print("                               ║         4-DÖVİZ UYGULAMASI                   ║") 
    print("                               ║                                              ║") 
    print("                               ║         5-Çıkış                              ║")
    print("                               ║                                              ║")
    print("                               ║          SEÇİMİNİ YAP!!                      ║")
    print("                               ╚══════════════════════════════════════════════╝")

    secim = input("Lütfen uygulama seçimini yapınız: ")


    if secim == "1":
        mesafe_birim.mesafemenu()
    elif secim == "2":
        oyunlar.oyunlarmenu()
    elif secim == "3":
        takvim.takvimmenu()
    elif secim == "4":
        doviz.dovizmenu()
    elif secim == "5":
        print("Çıkış yapılıyor...")
        exit()
    else:
        print("Geçersiz bir giriş yaptınız..")


anamenu()



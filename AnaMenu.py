import mesafe_birim
import oyunlar
import takvim
import doviz
import OS_ISLETIM
import BurcBulucu
import kilouygulamasi
import notOrtalamasi
import YazilimDilleri
import latin_arap

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
    print("                               ║         5-KİLO HESAPLAYICI                   ║")
    print("                               ║                                              ║")
    print("                               ║         6-NOT HESAPLAYICI                    ║")
    print("                               ║                                              ║")
    print("                               ║         7-LATİN-ARAP ALFABE ÇEVİRİCİ         ║")      
    print("                               ║                                              ║")      
    print("                               ║         8-YAZILIM DİLLERİ                    ║")      
    print("                               ║                                              ║")      
    print("                               ║         9-BURÇ BULUCU                        ║")      
    print("                               ║                                              ║")      
    print("                               ║         10-İŞLETİM SİSTEMLER                 ║")
    print("                               ║                                              ║")
    print("                               ║          SEÇİMİNİZİ YAPINIZ                  ║")
    print("                               ║                                              ║")
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
    elif secim=="5":
         kilouygulamasi.kilomenu()
    elif secim=="6":
         notOrtalamasi.not_ortalama_hesaplayici()
    elif secim=="7":
         latin_arap.latinArapMenu()
    elif secim=="8":
         YazilimDilleri.diller()
    elif secim== "9":
          BurcBulucu.burcmenu()
    elif secim== "10":
          OS_ISLETIM.isletim_sistemleri()
        
    else:
        print("Geçersiz bir giriş yaptınız..")

anamenu()



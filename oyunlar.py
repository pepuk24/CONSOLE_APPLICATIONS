import oyunlar_AdamAsmaca
import basit_tetris
def oyunlarmenu():
    print("\033[34m                                                                      ")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║")
    print("                               ║                 OYUNLAR                      ║")
    print("                               ║                                              ║")
    print("                               ╚══════════════════════════════════════════════╝")

    print("                               ╔══════════════════════════════════════════════╗")
    print("                               ║                                              ║") 
    print("                               ║                                              ║")
    print("                               ║                                              ║")
    print("                               ║                                              ║")
    print("                               ║               1-ADAM ASMACA                  ║")                             
    print("                               ║                                              ║")
    print("                               ║               2-TETRİS                       ║")
    print("                               ║                                              ║") 
    print("                               ║               3-ÇIKIŞ                        ║") 
    print("                               ║                                              ║") 
    print("                               ║                                              ║")
    print("                               ║                                              ║")
    print("                               ║             SEÇİMİNİ YAP!!                   ║")
    print("                               ╚══════════════════════════════════════════════╝")

    secim = input("Seçim yapınız: ")

    if secim=="1":  oyunlar_AdamAsmaca.adamasmacamenu()

    elif secim=="2":  basit_tetris.oyun()

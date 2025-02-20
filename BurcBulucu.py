def burcmenu():
        print("╔════════════════════════════════════════╗")
        print("║            BURÇ BULMA UYGULAMASI       ║")
        print("╚════════════════════════════════════════╝")

        gun = int(input("Doğduğunuz günü girin (1-31): "))
        ay = int(input("Doğduğunuz ayı girin (1-12): "))

        burclar = [
            ("Oğlak", (12, 22), (1, 19), "Disiplinli ve kararlı olma özellikleriyle bilinir."),
            ("Kova", (1, 20), (2, 18), "Bağımsız ve yenilikçi bir ruha sahiptir."),
            ("Balık", (2, 19), (3, 20), "Duygusal ve hayalperesttir."),
            ("Koç", (3, 21), (4, 19), "Lider ruhlu ve enerjik bir burçtur."),
            ("Boğa", (4, 20), (5, 20), "Sabırlı ve güvenilir yapısıyla tanınır."),
            ("İkizler", (5, 21), (6, 20), "Zeki ve iletişimci bir kişiliğe sahiptir."),
            ("Yengeç", (6, 21), (7, 22), "Duygusal ve koruyucu yapısıyla bilinir."),
            ("Aslan", (7, 23), (8, 22), "Liderlik vasfı yüksek ve cesurdur."),
            ("Başak", (8, 23), (9, 22), "Detaycı ve çalışkan bir burçtur."),
            ("Terazi", (9, 23), (10, 22), "Adaletli ve uyumlu yapısıyla bilinir."),
            ("Akrep", (10, 23), (11, 21), "Tutkulu ve kararlı bir yapıya sahiptir."),
            ("Yay", (11, 22), (12, 21), "Özgürlüğüne düşkün ve maceraperesttir.")
        ]

        bulunan_burc = None
        for burc, baslangic, bitis, aciklama in burclar:
            bas_ay, bas_gun = baslangic
            bit_ay, bit_gun = bitis

            if (ay == bas_ay and gun >= bas_gun) or (ay == bit_ay and gun <= bit_gun):
                bulunan_burc = (burc, aciklama)
                break

        if bulunan_burc:
            print(f"\nBurcunuz: {bulunan_burc[0]}")
            print(f"Özellikleri: {bulunan_burc[1]}")
        else:
            print("Geçersiz tarih girdiniz. Lütfen doğru bir tarih girin.")


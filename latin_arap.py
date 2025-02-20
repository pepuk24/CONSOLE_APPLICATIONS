def latinArapMenu():
    harf_haritasi = [
        ('a', 'ا'), ('b', 'ب'), ('c', 'ك'), ('d', 'د'), ('e', 'ﻩ'), ('f', 'ف'),
        ('g', 'ج'), ('h', 'ح'), ('i', 'ي'), ('j', 'ج'), ('k', 'ك'), ('l', 'ل'),
        ('m', 'م'), ('n', 'ن'), ('o', 'و'), ('p', 'پ'), ('q', 'ق'), ('r', 'ر'),
        ('s', 'س'), ('t', 'ت'), ('u', 'و'), ('v', 'ڤ'), ('w', 'و'), ('x', 'ﺥ'),
        ('y', 'ي'), ('z', 'ز'), (' ', ' ')
    ]

    kelime = input("Latin alfabesiyle bir harf girin: ").lower()
    ceviri = ''

    for harf in kelime:
        bulundu = False
        for latin, arap in harf_haritasi:
            if harf == latin:
                ceviri += arap
                bulundu = True
                break
        if not bulundu:
            ceviri += harf

    print("Arap alfabesiyle karşılığı:", ceviri)


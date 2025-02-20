def isletim_sistemleri():
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                  İŞLETİM SİSTEMLERİ LİSTESİ                ║")
    print("╠════════════════════════════════════════════════════════════╣")
    print("║ 1. Windows 10                  16. Chrome OS               ║")
    print("║ 2. Whonix                      17. FreeBSD                 ║")
    print("║ 3. macOS Sonoma                18. Solaris                 ║")
    print("║ 4. Ubuntu                      19. Qubes OS                ║")
    print("║ 5. Debian                      20. Tails OS                ║")
    print("║ 6. Fedora                      21. Zorin OS                ║")
    print("║ 7. Arch Linux                  22. Elementary OS           ║")
    print("║ 8. Linux Mint                  23. Pop!_OS                 ║")
    print("║ 9. Kali Linux                  24. OpenBSD                 ║")
    print("║ 10. Red Hat Enterprise Linux   25. ReactOS                 ║")
    print("║ 11. CentOS Stream              26. Haiku OS                ║")
    print("║ 12. OpenSUSE                   27. Mageia                  ║")
    print("║ 13. Manjaro                    28. Solus                   ║")
    print("║ 14. Gentoo                     29. Android                 ║")
    print("║ 15. Slackware                  30. iOS                     ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("SEÇİMİNİZ?")

    secim = input()

    sistemler = {
        "1": ["Windows 10", "4 GB", "Kişisel bilgisayarlar", "Modern arayüz, DirectX 12 desteği.", "Yaygın destek, oyun uyumluluğu.", "Lisans ücreti, sistem kaynaklarını fazla kullanır."],
        "2": ["Whonix", "4 GB", "Kişisel bilgisayarlar", "TOR ağı entegre", "Yüksek Anonimlik", "Sanal Makina Kullnımı Zorunluluğu ve Günlük kullnım için zor..."],
        "3": ["macOS Sonoma", "8 GB", "Apple bilgisayarlar", "Optimize edilmiş donanım uyumu.", "Yüksek stabilite, güvenlik.", "Sadece Apple cihazlarda çalışır."],
        "4": ["Ubuntu", "2 GB", "Masaüstü, sunucu", "GNOME masaüstü ortamı.", "Ücretsiz, geniş topluluk.", "Bazı sürücü uyumsuzlukları."],
        "5": ["Debian", "2 GB", "Sunucu, masaüstü", "Stabilite odaklı.", "Güvenilir, geniş paket havuzu.", "Yavaş güncellemeler."],
        "6": ["Fedora", "4 GB", "Masaüstü, geliştiriciler", "En yeni yazılımlar.", "Yenilikçi, ücretsiz.", "Kısa destek döngüsü."],
        "7": ["Arch Linux", "2 GB", "Geliştiriciler", "Rolling release modeli.", "Hafif ve özelleştirilebilir.", "Kurulumu karmaşık."],
        "8": ["Linux Mint", "2 GB", "Masaüstü", "Kullanıcı dostu arayüz.", "Yeni başlayanlar için ideal.", "Bazı eski yazılımlar."],
        "9": ["Kali Linux", "2 GB", "Siber güvenlik", "Penetrasyon test araçları.", "Güçlü araç seti.", "Günlük kullanım için uygun değil."],
        "10": ["Red Hat Enterprise Linux", "4 GB", "Kurumsal sunucu", "Uzun vadeli destek.", "Kurumsal destek.", "Lisans ücreti."],
        "11": ["CentOS Stream", "2 GB", "Sunucu", "RHEL'in geliştirme sürümü.", "Ücretsiz, RHEL'e yakın.", "Stabilite sorunları olabilir."],
        "12": ["OpenSUSE", "2 GB", "Masaüstü, sunucu", "Yast yapılandırma aracı.", "Kullanıcı dostu.", "Daha küçük topluluk."],
        "13": ["Manjaro", "2 GB", "Masaüstü", "Arch tabanlı.", "Kullanımı kolay Arch.", "Daha küçük topluluk."],
        "14": ["Gentoo", "4 GB", "Geliştiriciler", "Kaynak koddan derleme.", "Özelleştirilebilir.", "Kurulumu zor."],
        "15": ["Slackware", "2 GB", "Masaüstü", "Minimalist yapı.", "Esnek ve hafif.", "Kullanıcı dostu değil."],
        "16": ["Chrome OS", "4 GB", "Chromebook'lar", "Bulut odaklı sistem.", "Hızlı ve hafif.", "İnternete bağımlı."],
        "17": ["FreeBSD", "2 GB", "Sunucu, masaüstü", "ZFS desteği.", "Güçlü güvenlik.", "Az yazılım desteği."],
        "18": ["Solaris", "4 GB", "Kurumsal sunucu", "ZFS dosya sistemi.", "Yüksek stabilite.", "Azalan destek."],
        "19": ["Qubes OS", "4 GB", "Güvenlik odaklı", "Sanal makine temelli.", "Yüksek güvenlik.", "Performans ağır."],
        "20": ["Tails OS", "2 GB", "Anonimlik", "Tor ağı entegre.", "Yüksek gizlilik.", "Günlük kullanım için zor."],
        "21": ["Zorin OS", "2 GB", "Masaüstü", "Windows benzeri arayüz.", "Yeni başlayanlar için uygun.", "Sınırlı özelleştirme."],
        "22": ["Elementary OS", "2 GB", "Masaüstü", "macOS benzeri arayüz.", "Minimalist ve estetik.", "Sınırlı özelleştirme."],
        "23": ["Pop!_OS", "4 GB", "Geliştiriciler", "GNOME tabanlı.", "Donanım desteği güçlü.", "Bazı hatalar olabilir."],
        "24": ["OpenBSD", "2 GB", "Sunucu", "Güvenlik odaklı.", "Yüksek güvenlik.", "Az yazılım desteği."],
        "25": ["ReactOS", "2 GB", "Windows alternatifi", "Windows uyumlu.", "Açık kaynaklı.", "Eksik özellikler."],
        "26": ["Haiku OS", "2 GB", "Masaüstü", "BeOS tabanlı.", "Hafif ve hızlı.", "Az uygulama desteği."],
        "27": ["Mageia", "2 GB", "Masaüstü", "Mandriva tabanlı.", "Kullanıcı dostu.", "Küçük topluluk."],
        "28": ["Solus", "2 GB", "Masaüstü", "Bağımsız dağıtım.", "Modern ve hafif.", "Sınırlı paket havuzu."],
        "29": ["Android", "2 GB", "Mobil cihazlar", "Google Play desteği.", "Geniş uygulama ekosistemi.", "Güvenlik açıkları."],
        "30": ["iOS", "2 GB", "iPhone, iPad", "App Store desteği.", "Yüksek güvenlik.", "Kapalı ekosistem."]
    }

    if secim in sistemler:
        info = sistemler[secim]
        print("\nİşletim Sistemi Bilgileri:")
        print(f"Adı: {info[0]}")
        print(f"Minimum RAM: {info[1]}")
        print(f"Kullanım Alanı: {info[2]}")
        print(f"Özellikler: {info[3]}")
        print(f"Avantajları: {info[4]}")
        print(f"Dezavantajları: {info[5]}")
    else:
        print("Geçersiz seçim! Lütfen listedeki numaralardan birini girin.")


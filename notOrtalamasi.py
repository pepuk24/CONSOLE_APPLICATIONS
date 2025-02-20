def not_ortalama_hesaplayici():
    print("╔═════════════════════════════════╗")
    print("║      Not Ortalaması Hesapla     ║")
    print("╚═════════════════════════════════╝")
    
    ders_sayisi = int(input("Kaç dersin notunu gireceksiniz?: "))
    toplam_not = 0

    for i in range(1, ders_sayisi + 1):
        not_girisi = float(input(f"{i}. dersin notunu girin: "))
        toplam_not += not_girisi

    ortalama = toplam_not / ders_sayisi
    print(f"Not ortalamanız: {ortalama:.2f}")

    # Ek işlemler
    print("\nEk işlemler:")
    print(f"Ortalamanın karesi: {ortalama ** 2}")
    print(f"Ortalamanın küpü: {ortalama ** 3}")
    print(f"Ortalamanın 5'e göre modu: {ortalama % 5}")

if __name__ == "__main__":
    not_ortalama_hesaplayici()


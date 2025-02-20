import pygame
import random
import sys

def oyun():
    # Pygame başlat
    pygame.init()

    # Oyun ayarları
    GENISLIK, YUKSEKLIK = 200, 400
    KARE_BOYUTU = 20
    FPS = 30

    ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    pygame.display.set_caption("Tetris")

    # Renkler
    SIYAH = (0, 0, 0)
    MAVI = (0, 0, 255)
    KIRMIZI = (255, 0, 0)

    saat = pygame.time.Clock()

    # Sabitlenmiş bloklar
    sabit_bloklar = []

    # Blok oluştur
    def yeni_blok():
        x = GENISLIK // 2
        y = 0
        renk = random.choice([MAVI, KIRMIZI])
        return [x, y, renk]

    blok = yeni_blok()

    # Çarpışma kontrolü
    def carpisma(x, y):
        if y + KARE_BOYUTU > YUKSEKLIK:
            return True
        for b in sabit_bloklar:
            if b[0] == x and b[1] == y + KARE_BOYUTU:
                return True
        return False

    calisiyor = True
    while calisiyor:
        ekran.fill(SIYAH)

        # Olaylar
        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif etkinlik.type == pygame.KEYDOWN:
                if etkinlik.key == pygame.K_LEFT and blok[0] - KARE_BOYUTU >= 0:
                    if not carpisma(blok[0] - KARE_BOYUTU, blok[1]):
                        blok[0] -= KARE_BOYUTU
                elif etkinlik.key == pygame.K_RIGHT and blok[0] + KARE_BOYUTU < GENISLIK:
                    if not carpisma(blok[0] + KARE_BOYUTU, blok[1]):
                        blok[0] += KARE_BOYUTU
                elif etkinlik.key == pygame.K_DOWN:
                    if not carpisma(blok[0], blok[1] + KARE_BOYUTU):
                        blok[1] += KARE_BOYUTU

        # Blok düşürme
        if not carpisma(blok[0], blok[1] + 1):
            blok[1] += 1
        else:
            sabit_bloklar.append([blok[0], blok[1], blok[2]])
            blok = yeni_blok()
            if carpisma(blok[0], blok[1]):
                print("Oyun Bitti!")
                pygame.quit()
                sys.exit()

        # Sabit blokları çiz
        for b in sabit_bloklar:
            pygame.draw.rect(ekran, b[2], (b[0], b[1], KARE_BOYUTU, KARE_BOYUTU))

        # Hareket eden bloğu çiz
        pygame.draw.rect(ekran, blok[2], (blok[0], blok[1], KARE_BOYUTU, KARE_BOYUTU))

        pygame.display.flip()
        saat.tick(FPS)


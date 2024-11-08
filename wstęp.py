import pygame
import sys

from gra import Game

pygame.init()

szerokosc_okna = 900
wysokosc_okna = 600
window = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
pygame.display.set_caption("Gra")

czcionka1 = pygame.font.SysFont('couriernew',40)
czcionka2 = pygame.font.SysFont('couriernew',28)

while True:
    window.fill((0, 0, 0))  

    napis1 = czcionka1.render("Zasady Gry:", True, (255, 255, 255))  
    napis2 = czcionka2.render("-Poruszaj się ludzikiem strzałkami lewo, prawo", True, (255, 255, 255)) 
    napis3 = czcionka2.render("-Aby skakać między platformami używaj spacji", True, (255, 255, 255))
    napis4 = czcionka2.render("-Gra kończy gdy wskoczysz na ostatnią platformę", True, (255, 255, 255)) 
    napis5 = czcionka1.render("Aby rozpocząć kliknij ENTER", True, (255, 255, 255)) 

    pozycja1 = napis1.get_rect(center=(szerokosc_okna // 2, wysokosc_okna // 2 - 150))  
    window.blit(napis1, pozycja1.topleft)

    pozycja2 = napis2.get_rect(center=(szerokosc_okna // 2, wysokosc_okna // 2 - 100))  
    window.blit(napis2, pozycja2.topleft + (0, 50))  

    pozycja3 = napis3.get_rect(center=(szerokosc_okna // 2, wysokosc_okna // 2 - 50))  
    window.blit(napis3, pozycja3.topleft + (0, 100))

    pozycja4 = napis4.get_rect(center=(szerokosc_okna // 2, wysokosc_okna // 2 ))  
    window.blit(napis4, pozycja4.topleft + (0, 150))  

    pozycja5 = napis5.get_rect(center=(szerokosc_okna // 2, wysokosc_okna // 2 + 50))  
    window.blit(napis5, pozycja5.topleft + (0, 200))  

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                lvl1 = Game()
                lvl1.run()
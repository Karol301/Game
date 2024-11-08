import pygame
import sys 



class Koniec:
    def __init__(self):

        szerokosc_okna = 900
        wysokosc_okna = 600
        window = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
        pygame.display.set_caption("Gra")

        czcionka1 = pygame.font.SysFont('couriernew',40)
        czcionka2 = pygame.font.SysFont('couriernew',28)

        while True:
            window.fill((0, 0, 0))  

            napis1 = czcionka1.render("Gratulacje Wygrałeś!", True, (255, 255, 255)) 
            napis2 = czcionka2.render("Space - Zamknij", True, (255, 255, 255))   
            
            pozycja1 = napis1.get_rect(center=(szerokosc_okna // 2, wysokosc_okna // 2 - 100))  
            window.blit(napis1, pozycja1.topleft)

            pozycja2 = napis2.get_rect(center=(szerokosc_okna // 2, wysokosc_okna // 2))  
            window.blit(napis2, pozycja2.topleft)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                     
                    if event.key == pygame.K_SPACE:
                        pygame.quit()
                        sys.exit()
import pygame, sys

from koniec import Koniec

class Lvl2:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Gra")
        self.window = pygame.display.set_mode((900,700))
        self.clock = pygame.time.Clock()
    
        self.niebo2 = pygame.image.load("zdjęcia/niebo2_gra.png")
        self.ziemia2 = pygame.image.load("zdjęcia/ziemia2_gra.png")

        self.ludzik_img = pygame.image.load("zdjęcia/postać_gra.png")
        self.ludzik_img.set_colorkey((255, 255, 255))
        self.ludzik = pygame.transform.scale(self.ludzik_img, (60,50))
        self.ludzik_rect = self.ludzik.get_rect(midbottom = (100, 600))
        

        #przeskody
        poziom1 = pygame.image.load("zdjęcia/poziom2_gra.png")
        self.poziom1 = pygame.transform.scale(poziom1 ,(100,30))
        self.poziom1_rect = self.poziom1.get_rect(midbottom = (300,580))

        poziom2 = pygame.image.load("zdjęcia/poziom2_gra.png")
        self.poziom2 = pygame.transform.scale(poziom2 ,(100,30))
        self.poziom2_rect = self.poziom2.get_rect(midbottom = (400,490))

        poziom3 = pygame.image.load("zdjęcia/poziom2_gra.png")
        self.poziom3 = pygame.transform.scale(poziom3 ,(100,30))
        self.poziom3_rect = self.poziom3.get_rect(midbottom = (480,400))

        poziom4 = pygame.image.load("zdjęcia/poziom2_gra.png")
        self.poziom4 = pygame.transform.scale(poziom4 ,(100,30))
        self.poziom4_rect = self.poziom4.get_rect(midbottom = (380,300))

        poziom5 = pygame.image.load("zdjęcia/poziom2_gra.png")
        self.poziom5 = pygame.transform.scale(poziom5 ,(100,30))
        self.poziom5_rect = self.poziom5.get_rect(midbottom = (440, 200))

        poziom6 = pygame.image.load("zdjęcia/meta_gra2.png")
        self.poziom6 = pygame.transform.scale(poziom6 ,(100,30))
        self.poziom6_rect = self.poziom6.get_rect(midbottom = (580,140))

        self.text = pygame.image.load("zdjęcia/lvl2.png")
        self.text.set_colorkey((255, 255, 255))
        self.text = pygame.transform.scale(self.text, (120,80))

        self.ludzik_movemet = [0]
        self.ludzik_gravity = 0

        self.poz1 = False
        self.poz2 = False
        self.poz3 = False
        self.poz4 = False
        self.poz5 = False
        self.poz6 = False

    def run(self):
        while True:
            
            czcionka = pygame.font.SysFont('Arial', 36)
            self.ludzik_gravity += 1
            self.ludzik_rect.y += self.ludzik_gravity

            if self.ludzik_rect.bottom >= 600:
                self.ludzik_rect.bottom = 600

            #1
            if self.ludzik_rect.top < self.poziom1_rect.bottom and self.ludzik_rect.right > self.poziom1_rect.left and self.ludzik_rect.left < self.poziom1_rect.right and self.ludzik_rect.bottom >= 550:
                self.poz1 = True
            else:
                self.poz1 = False

            #2
            if self.ludzik_rect.top < self.poziom2_rect.bottom and self.ludzik_rect.right > self.poziom2_rect.left and self.ludzik_rect.left < self.poziom2_rect.right and self.ludzik_rect.bottom > 450 and self.ludzik_rect.bottom < 490:
                self.ludzik_gravity = 0
                self.poz2 = True 
            elif self.ludzik_rect.colliderect(self.poziom2_rect):
                if self.ludzik_rect.top <= self.poziom2_rect.bottom and self.ludzik_rect.bottom > self.poziom2_rect.bottom and self.ludzik_rect.bottom >= 440:
                    self.ludzik_rect.bottom += 50 
            else:
                self.poz2 = False 
            
            #3
            if self.ludzik_rect.top < self.poziom3_rect.bottom and self.ludzik_rect.right > self.poziom3_rect.left and self.ludzik_rect.left < self.poziom3_rect.right and self.ludzik_rect.bottom > 360 and self.ludzik_rect.bottom < 400:
                self.ludzik_gravity = 0
                self.poz3 = True 
            elif self.ludzik_rect.colliderect(self.poziom3_rect):
                if self.ludzik_rect.top <= self.poziom3_rect.bottom and self.ludzik_rect.bottom > self.poziom3_rect.bottom and self.ludzik_rect.bottom >= 360:
                    self.ludzik_rect.bottom += 50
            else:
                self.poz3 = False
            
            #4
            if self.ludzik_rect.top < self.poziom4_rect.bottom and self.ludzik_rect.right > self.poziom4_rect.left and self.ludzik_rect.left < self.poziom4_rect.right and self.ludzik_rect.bottom > 260 and self.ludzik_rect.bottom < 300:
                self.ludzik_gravity = 0
                self.poz4 = True 
            elif self.ludzik_rect.colliderect(self.poziom4_rect):
                if self.ludzik_rect.top <= self.poziom4_rect.bottom and self.ludzik_rect.bottom > self.poziom4_rect.bottom and self.ludzik_rect.bottom >= 260:
                    self.ludzik_rect.bottom += 50
            else:
                self.poz4 = False

            #5
            if self.ludzik_rect.top < self.poziom5_rect.bottom and self.ludzik_rect.right > self.poziom5_rect.left and self.ludzik_rect.left < self.poziom5_rect.right and self.ludzik_rect.bottom > 160 and self.ludzik_rect.bottom < 200:
                self.ludzik_gravity = 0
                self.poz5 = True 
            elif self.ludzik_rect.colliderect(self.poziom5_rect):
                if self.ludzik_rect.top <= self.poziom5_rect.bottom and self.ludzik_rect.bottom > self.poziom5_rect.bottom and self.ludzik_rect.bottom >= 160:
                    self.ludzik_rect.bottom += 50
            else:
                self.poz5 = False
            
            #6
            if self.ludzik_rect.top < self.poziom6_rect.bottom and self.ludzik_rect.right > self.poziom6_rect.left and self.ludzik_rect.left < self.poziom6_rect.right and self.ludzik_rect.bottom >= 100 and self.ludzik_rect.bottom < 140:
                self.ludzik_gravity = 0
                self.poz6 = True 
            elif self.ludzik_rect.colliderect(self.poziom6_rect):
                if self.ludzik_rect.top <= self.poziom6_rect.bottom and self.ludzik_rect.bottom > self.poziom6_rect.bottom and self.ludzik_rect.bottom >= 100:
                    self.ludzik_rect.bottom += 50
            else:
                self.poz6 = False
            
            if self.poz1: 
                self.ludzik_rect.bottom = self.poziom1_rect.top
            
            if self.poz2:       
                self.ludzik_rect.bottom = self.poziom2_rect.top
            
            if self.poz3:       
                self.ludzik_rect.bottom = self.poziom3_rect.top

            if self.poz4:       
                self.ludzik_rect.bottom = self.poziom4_rect.top
            
            if self.poz5:       
                self.ludzik_rect.bottom = self.poziom5_rect.top
            
            if self.poz6:            
                self.ludzik_rect.bottom = self.poziom6_rect.top

                koniec = Koniec()
                koniec.run()                

            self.ludzik_rect[0] += self.ludzik_movemet[0]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ludzik_movemet[0] = 3
                    if event.key == pygame.K_LEFT:
                        self.ludzik_movemet[0] = -3
                    if self.ludzik_rect.bottom == 600 and event.key == pygame.K_SPACE:
                        self.ludzik_gravity = -15
                    if self.ludzik_rect.bottom == self.poziom1_rect.top and event.key == pygame.K_SPACE:
                        self.ludzik_gravity = -15
                    if self.ludzik_rect.bottom == self.poziom2_rect.top and event.key == pygame.K_SPACE:
                        self.ludzik_gravity = -15
                    if self.ludzik_rect.bottom == self.poziom3_rect.top and event.key == pygame.K_SPACE:
                        self.ludzik_gravity = -15
                    if self.ludzik_rect.bottom == self.poziom4_rect.top and event.key == pygame.K_SPACE:
                        self.ludzik_gravity = -15
                    if self.ludzik_rect.bottom == self.poziom5_rect.top and event.key == pygame.K_SPACE:
                        self.ludzik_gravity = -15
                   
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ludzik_movemet[0] = 0
                    if event.key == pygame.K_LEFT:
                        self.ludzik_movemet[0] = 0   
                
            if self.ludzik_rect[0] <= 0 or self.ludzik_rect[0] >= 900:
                self.ludzik_rect[0] = 100  
               
            self.window.blit(self.niebo2, (0,0))
            self.window.blit(self.ziemia2, (0,600))

            self.window.blit(self.text, (400,50))
            

            self.window.blit(self.poziom1, self.poziom1_rect)
            self.window.blit(self.poziom2, self.poziom2_rect)
            self.window.blit(self.poziom3, self.poziom3_rect)
            self.window.blit(self.poziom4, self.poziom4_rect)
            self.window.blit(self.poziom5, self.poziom5_rect)

            self.window.blit(self.poziom6, self.poziom6_rect)

            self.window.blit(self.ludzik, self.ludzik_rect)

            #warunki kolizji lewo prawo
            if self.ludzik_rect.colliderect(self.poziom1_rect):
                if self.ludzik_rect.right >= self.poziom1_rect.left and self.ludzik_rect.left <= self.poziom1_rect.right and self.ludzik_rect.left < 300:
                    self.ludzik_rect.left -= 100

                elif self.ludzik_rect.right >= self.poziom1_rect.left and self.ludzik_rect.left <= self.poziom1_rect.right and self.ludzik_rect.left > 270:
                    self.ludzik_rect.right += 100

            elif self.ludzik_rect.colliderect(self.poziom2_rect):
                if self.ludzik_rect.right >= self.poziom2_rect.left and self.ludzik_rect.left <= self.poziom2_rect.right and self.ludzik_rect.left < 400:
                    self.ludzik_rect.right -= 100
                
                elif self.ludzik_rect.right >= self.poziom2_rect.left and self.ludzik_rect.left <= self.poziom2_rect.right and self.ludzik_rect.left > 370:
                    self.ludzik_rect.right += 100
            
            elif self.ludzik_rect.colliderect(self.poziom3_rect):
                if self.ludzik_rect.right >= self.poziom3_rect.left and self.ludzik_rect.left <= self.poziom3_rect.right and self.ludzik_rect.left < 480:
                    self.ludzik_rect.right -= 100
                
                elif self.ludzik_rect.right >= self.poziom3_rect.left and self.ludzik_rect.left <= self.poziom3_rect.right and self.ludzik_rect.left > 480:
                    self.ludzik_rect.right += 100
            
            elif self.ludzik_rect.colliderect(self.poziom4_rect):
                if self.ludzik_rect.right >= self.poziom4_rect.left and self.ludzik_rect.left <= self.poziom4_rect.right and self.ludzik_rect.left < 380:
                    self.ludzik_rect.right -= 100
                
                elif self.ludzik_rect.right >= self.poziom4_rect.left and self.ludzik_rect.left <= self.poziom4_rect.right and self.ludzik_rect.left > 380:
                    self.ludzik_rect.right += 100            

            pygame.display.update()
            self.clock.tick(70)       


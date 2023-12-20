import pygame
import sys

#Makes basic window for game
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH*0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GAME1")

#Created class for soldier so reuse for other enemies
class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('player/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        #creates collusion on img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

#Cordinates for player start and scale size of character    
player = Soldier(200, 200, 3)
player_speed = 5


#While loop for game to not auto quit, if stament for user to quit game
run = True
while run:

    #draws img on the window
    screen.blit(player.image, player.rect)


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.rect.x += player_speed
    pygame.display.flip()
    if keys[pygame.K_DOWN]:
        player.rect.y += player_speed
    if keys[pygame.K_UP]:
        player.rect.y -= player_speed
    
    pygame.display.flip()

pygame.quit()
sys.exit()

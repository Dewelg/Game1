import pygame

#Makes basic window for game
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH*0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GAME1")

#Cordinates for player start
x = 200
y = 200
img = pygame.image.load('img/player/Idle/0.png')
#creates collusion on img
rec = img.get_rect()
rec.center = (x,y)

#While loop for game to not auto quit, if stament for user to quit game
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()


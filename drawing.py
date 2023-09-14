#V1.0
#by hatsfornone
import pygame

pygame.init()
#colors
white = (255,255,255)
black = (0,0,0)

#misc
run = True
clock = pygame.time.Clock()

#screen
screen = pygame.display.set_mode((720,480))
pygame.display.set_caption("drawing")
screen.fill(black)
#classe(s)
class cursor:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.lenght = height
#misc2
cursor_x = -10
cursor_y = -10
while run:
    #controls
    key = pygame.key.get_pressed()
    
    if key[pygame.K_SPACE] == True:
        cursor_x, cursor_y = pygame.mouse.get_pos()
    if key[pygame.K_c] == True:
        screen.fill(black)
        cursor_x = -10
        cursor_y = -10
    #class setup
    cursor_setup = cursor(cursor_x,cursor_y,10,10)
    #load and draw objects
    CURSOR=pygame.Rect(cursor_setup.x,cursor_setup.y,cursor_setup.width,cursor_setup.lenght)
    pygame.draw.rect(screen,white,CURSOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(120)
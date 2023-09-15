#V2.5
#by hatsfornone
import pygame

pygame.init()
#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
#misc
run = True
clock = pygame.time.Clock()

#screen
screen = pygame.display.set_mode((720,480))
pygame.display.set_caption("drawing")
screen.fill(black)
#classe(s)
class cursor:
    def __init__(self,x,y,radius,width):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width
#cursor
cursor_x, cursor_y = (-10,-10) #cursor needs a starting value
cursor_color = white #starting color
while run:
    #get input
    key = pygame.key.get_pressed()
    #clear and draw
    if pygame.mouse.get_pressed()[0] == True:
        cursor_x, cursor_y = pygame.mouse.get_pos()
    if key[pygame.K_SPACE] or key[pygame.K_c] == True:
        screen.fill(black)
        cursor_x = -10
        cursor_y = -10
    #change color 
    if key[pygame.K_r] == True:
        cursor_color = red
        cursor_x = -10
        cursor_y = -10
    if key[pygame.K_w] == True:
        cursor_color = white
        cursor_x = -10
        cursor_y = -10 
    if key[pygame.K_g] == True:
        cursor_color = green
        cursor_x = -10
        cursor_y = -10
    if key[pygame.K_b] == True:
        cursor_color = blue
        cursor_x = -10
        cursor_y = -10
    
    #class setup
    cursor_setup = cursor(cursor_x,cursor_y,10,10) #change last 2 numbers to change cursor radius and width
    #load and/or draw objects
    pygame.draw.circle(screen,cursor_color,(cursor_x,cursor_y),cursor_setup.radius,cursor_setup.width)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(120)

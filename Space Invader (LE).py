#----------------------------------------------------------------------------
#                       Chapter 11 Homework: Space Invader 
#
#       Created by: Andy
#       Created on: March 11, 2020
#
#----------------------------------------------------------------------------

import pygame
import sys
import time
import random

from pygame.locals import *

import pygame

def main():

    pygame.init()

    #Set the width and height of the screen [width,height]
    size = [900, 600]
    screen = pygame.display.set_mode(size)

    #screen_width = 900
    #screen_height = 600
    #screen = pygame.display.set_mode((screen_width, screen_height))
    
    fps = 60
    fpsClock = pygame.time.Clock()

    pygame.display.set_caption("Space Invaders")

    background_image = pygame.image.load("cosmo.png")

    player_image = pygame.image.load("space_ship.png")

    #Define some colors
    BLACK = (0, 0, 0)
    PURPLE = (192, 19, 187)
    BLUE = (18, 229, 226)
    YELLOW = (228, 243, 4)
    ORANGE = (243, 178, 4)
    RED = (250, 0, 0)
    WHITE = (255, 255, 255)

    #Spaceship
    spaceship = pygame.rect.Rect(430, 500, 50, 50)

    #Variables here
    #Aliens' speed
    x_speed = 3

    #Spaceship's speed
    xspeed = 5
    yspeed = 5

    #Alien Startin position
    alien1x = 0
    alien2x = 0
    alien3x = 0
    
    alien4x = 110
    alien5x = 110
    alien6x = 110

    alien7x = 220
    alien8x = 220
    alien9x = 220

    alien10x = 330
    alien11x = 330
    alien12x = 330

    alien13x = 440
    alien14x = 440
    alien15x = 440

    alien16x = 550
    alien17x = 550
    alien18x = 550

    alien19x = 660
    alien20x = 660
    alien21x = 660

    alien22x = 770
    alien23x = 770
    alien24x = 770
    

    row1y = 20
    row2y = 140
    row3y = 260

    #Score & Life
    #score = 0
    #life = 3

    #def invader(x,y):
        #screen.blit(player_image, (x,y))

    #x = (screen_width * 0.42)
    #y = (screen_height * 0.66)
    
    display_width = 900
    display_height = 600

    screen = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Space Invader")

    clock = pygame.time.Clock()
    done = False
    
    def spaceship(x,y):
        screen.blit(player_image, (x,y))

    x = (display_width * 0.385)
    y = (display_height * 0.8)

    x_change = 0
    
    #Game loop
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
              pygame.quit()
              sys.exit()
              
        #screen.blit(background_image, [0,0])
        #invader(x,y)

        #pygame.display.update()
        #fpsClock = pygame.time.Clock()

            #Controls here
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    #spaceship.x -= 30
                    x_change = -5
                   
                elif event.key== pygame.K_RIGHT:
                    #spaceship.x += 30
                    x_change = 5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        x += x_change       
        screen.blit(background_image, [0, 0])
        spaceship(x,y)
                
                   
        #Drawing stuff
        #Loading up image file and cutting the sprite sheet and audio
        background_image = pygame.image.load("cosmo.png")
        
        player_image = pygame.image.load("space_ship.png")

        sprite_sheet = pygame.image.load("invaders.png")

        laser_sound = pygame.mixer.Sound("laser5.ogg")

        alien_type1 = sprite_sheet.subsurface(380, 40, 100, 85)

        #Drawing
        screen.blit(background_image, [0,0])
        screen.blit(player_image, (x, y)) 

        #Row 1 (row1y)
        alien1x += x_speed
        screen.blit(alien_type1, [alien1x, row1y])
        alien4x += x_speed
        screen.blit(alien_type1, [alien4x, row1y])
        alien7x += x_speed
        screen.blit(alien_type1, [alien7x, row1y])
        alien10x += x_speed
        screen.blit(alien_type1, [alien10x, row1y])
        alien13x += x_speed
        screen.blit(alien_type1, [alien13x, row1y])
        alien16x += x_speed
        screen.blit(alien_type1, [alien16x, row1y])
        alien19x += x_speed
        screen.blit(alien_type1, [alien19x, row1y])
        alien22x += x_speed
        screen.blit(alien_type1, [alien22x, row1y])
        
        #Row 2 (row2y)
        alien2x += x_speed
        screen.blit(alien_type1, [alien2x, row2y])
        alien5x += x_speed
        screen.blit(alien_type1, [alien5x, row2y])
        alien8x += x_speed
        screen.blit(alien_type1, [alien8x, row2y])
        alien11x += x_speed
        screen.blit(alien_type1, [alien11x, row2y])
        alien14x += x_speed
        screen.blit(alien_type1, [alien14x, row2y])
        alien17x += x_speed
        screen.blit(alien_type1, [alien17x, row2y])
        alien20x += x_speed
        screen.blit(alien_type1, [alien20x, row2y])
        alien23x += x_speed
        screen.blit(alien_type1, [alien23x, row2y])

        #Row 3 (row3y)
        alien3x += x_speed
        screen.blit(alien_type1, [alien3x, row3y])
        alien6x += x_speed
        screen.blit(alien_type1, [alien6x, row3y])
        alien9x += x_speed
        screen.blit(alien_type1, [alien9x, row3y])
        alien12x += x_speed
        screen.blit(alien_type1, [alien12x, row3y])
        alien15x += x_speed
        screen.blit(alien_type1, [alien15x, row3y])
        alien18x += x_speed
        screen.blit(alien_type1, [alien18x, row3y])
        alien21x += x_speed
        screen.blit(alien_type1, [alien21x, row3y])
        alien24x += x_speed
        screen.blit(alien_type1, [alien24x, row3y])

        #This detectes if the aliens are touching the sides or not
        if (alien22x + 100 >= 900) or (alien1x <= 0):
            x_speed = -x_speed
            #row1y += 10
            #row2y += 10
            #row3y += 10
            
        
        #Spaceship
        #pygame.draw.rect(screen, RED, spaceship)
        
        pygame.display.flip()
        fpsClock.tick(fps)
        time.sleep(0.05)

main()



##Instruction for drawing
##put your starting x coord in staring position
##name the variable 'alien(number)x'
##go to the row you want
##plus x_speed
##blit it with alien_type1
#They must be 102 pixel side to side in one row.


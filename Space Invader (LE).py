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

import random

   

def main():

    pygame.init()

    #Set the width and height of the screen [width,height]
    size = [900, 600]
    screen = pygame.display.set_mode(size)
    
    fps = 60
    fpsClock = pygame.time.Clock()

    pygame.display.set_caption("Space Invaders")

    background_image = pygame.image.load("cosmo.png").convert_alpha()

    player_image = pygame.image.load("space_ship.png").convert_alpha()

    laser_beam = pygame.image. load("laser_beam.png").convert_alpha()

    #Define some colors
    BLACK = (0, 0, 0)
    PURPLE = (192, 19, 187)
    BLUE = (18, 229, 226)
    YELLOW = (228, 243, 4)
    ORANGE = (243, 178, 4)
    RED = (250, 0, 0)
    WHITE = (255, 255, 255)

    #Variables here
    #Aliens' speed
    x_speed = 3

    #Spaceship's speed
    xspeed = 5
    yspeed = 5

    life = True
    score = 0

    
    laserx = 0
    lasery = 0
    again = True

    bulletx = 0
    bullety = 0
    shoot = True

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

    alien_list = [[alien1x, row1y],[alien4x, row1y],[alien7x, row1y],[alien10x, row1y],[alien13x, row1y],[alien16x, row1y],[alien19x, row1y],[alien22x, row1y],[alien2x, row2y],[alien5x, row2y],[alien8x, row2y],[alien11x, row2y],[alien14x, row2y],[alien17x, row2y],[alien20x, row2y],[alien23x, row2y],[alien3x, row3y],[alien6x, row3y],[alien9x, row3y],[alien12x, row3y],[alien15x, row3y],[alien18x, row3y],[alien21x, row3y],[alien24x, row3y]]


    
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

    def alien(x,y):
        screen.blit(alien_type1, [x, y])

    def alien_update(x):
        x+=x_speed
        return x
        
    def laser(x,y):
        screen.blit(laser_beam, [335, 485])

    def texts(score,location_x,location_y,text,colour,size):
       font=pygame.font.Font(None,size)
       scoretext=font.render(text+str(score), 1,colour)
       screen.blit(scoretext, (location_x, location_y))

    #Drawing stuff
    #Loading up image file and cutting the sprite sheet and audio

    background_image = pygame.image.load("cosmo.png").convert_alpha()
        
    ship = pygame.image.load("space_ship.png").convert_alpha()

    sprite_sheet = pygame.image.load("invaders.png").convert_alpha()

    laser_beam = pygame.image. load("laser_beam.png").convert_alpha()

    laser_sound = pygame.mixer.Sound("laser5.ogg")

    alien_type1 = sprite_sheet.subsurface(380, 40, 100, 85)

    player_image = ship.subsurface(260,175,320,253)

    
    
    #Game loop
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
              pygame.quit()
              sys.exit()            

            #Controls here
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -10
                   
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


                    

        #Loser statement
        if life == False:
            screen.blit(background_image, [0,0])
            texts('',200,230,"GAME OVER",WHITE,120)
        #This check if its gameover or not
        if life == True:
                    
            x += x_change       
            spaceship(x,y)

            #Drawing
            screen.blit(background_image, [0,0])
            screen.blit(player_image, (x, y))
            screen.blit(laser_beam, [335, 485])

            if again == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        again = False

            #This updates x of aliex
            for coord in (alien_list):
                new_alienx = alien_update(coord[0])
                coord[0] = new_alienx

            #This draws the aliens
            for coord in (alien_list):
                alien(coord[0],coord[1])

            #This draw alien bullet
            if shoot == True:
                for coord in (alien_list):
                    luck = random.randint(1,200)
                    if luck == 2:
                        bullety = int(coord[1]+42)
                        bulletx = int(coord[0]+40)
                        shoot = False
                        
            #Updates alien bullet
            if shoot == False:
                bullety += 10
                pygame.draw.circle(screen, BLUE, (bulletx, bullety), 10)
                
            #Check if it is off the screen
            if bullety >= 600:
                shoot = True

            #This check if it collides with the spaceship
            if (bullety <= y + 1) and (bullety + 10 >= y):
                if (bulletx + 15 >= x) and (bulletx <= x + 160):
                    shoot = True
                    life = False

            #This updates the laser
            if again == True:
                lasery = int(y)
                laserx = int(x + 140)           

            if again == False:
                lasery -= 10
                pygame.draw.circle(screen, WHITE, (laserx, lasery), 10)

            if lasery <= -10:
                again = True

            #This detectes if the aliens are touching the sides or not
            for coord in alien_list:
                if (coord[0] <= 0) or (coord[0] +100 >= 900):
                    x_speed = -x_speed

            #This detects if it hits or not
            for coord in (alien_list):
                if (lasery + 10 >= coord[1] + 85) and (lasery <= coord[1] + 85):
                    if (laserx + 10 >= coord[0]) and (laserx <= coord[0] + 100):
                        alien_list.remove(coord)
                        again = True
                        
        #Winner statment
        if alien_list == []:
            texts('',300,230,"YOU WIN",WHITE,120)
            
        #Updating the screen
        pygame.display.flip()
        fpsClock.tick(fps)
        time.sleep(0.05)

main()

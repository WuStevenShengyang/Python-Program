import pygame
import math
from pygame.locals import *
 

import random
pygame.init()

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]

def main():
                
    w = pygame.display.set_mode((300,300))
    w.fill(BLACK)

    c = pygame.time.Clock()
    game = True

    #Def player1
    player_1_speed = 0
    player_1_y = 100

    #Def player2
    player_2_speed = 0
    player_2_y = 100
    
    #Def ball
    ball_speedx = 3
    ball_speedy = 3
    
    
    
    ball_x = 100
    ball_y = 150

    #Main Loop
    while game:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_1_speed = -4
                if event.key == pygame.K_s:
                    player_1_speed = 4

        #Computer Move   
        if player_2_y+25 <= ball_y:
            player_2_speed = 2
        elif player_2_y+25 > ball_y:
            player_2_speed = -2

        #Draw two players and move the ball
        player_1_y = draw_player_1(player_1_speed,player_1_y)
        player_2_y = draw_player_2(player_2_speed,player_2_y)
        ball_x, ball_y = draw_ball(ball_speedx, ball_speedy, ball_x, ball_y)
        draw_border()
        
        #Win Condition
        if ball_x >= 300:
            game = False
            print("You win!")
            again()
        elif ball_x <= 0:
            game = False
            print("Computer win!")
            again()
            
        if ball_y >= 300 or ball_y <= 0:
            ball_speedy *= -1
            ball_speedy += random.randint(-1,1)
        
        #Ball Bounce when hit player
        if ball_x >= 290 and ball_y >= player_2_y and ball_y <= player_2_y+50:
            ball_speedx *= -1
        if ball_x <= 10 and ball_y >= player_1_y and ball_y <= player_1_y+50:
            ball_speedx *= -1

            
        pygame.display.flip()
        w.fill((BLACK))
        c.tick(30)
        
def draw_border():
    rect_p1 = pygame.Rect(0,0,2,300)
    rect_p2 = pygame.Rect(298,0,2,300)

    window = pygame.display.get_surface()
    pygame.draw.rect(window, RED, rect_p1)
    pygame.draw.rect(window, RED, rect_p2)
    
def draw_ball(speedx, speedy, xpos, ypos):
    
    xpos += speedx
    ypos += speedy
    
    window = pygame.display.get_surface()
    pygame.draw.circle(window,WHITE,(xpos,ypos),5,5)
    
    return xpos, ypos

def draw_player_1(speed1,ypos):               
    if (ypos+50) >= 300:
        speed1 = 0
        ypos -= 1
    elif ypos <= 0:
        speed1 = 0
        ypos += 1
               
    rect = pygame.Rect(2,ypos,10,50)
    
    ypos += speed1

    window = pygame.display.get_surface()
    pygame.draw.rect(window,WHITE,rect)
    

    return ypos

def draw_player_2(speed2,ypos):
    if (ypos+50) >= 300:
        speed2 = 0
        ypos -= 1
    elif ypos <= 0:
        speed2 = 0
        ypos += 1
               
    rect = pygame.Rect(288,ypos,10,50)
    ypos += speed2

    window = pygame.display.get_surface()
    pygame.draw.rect(window,WHITE,rect)

    return ypos

def again():
    trying = True
    while trying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                trying = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main()

if __name__ == "__main__":
    main()

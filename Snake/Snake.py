import pygame
import random

pygame.init()
w=pygame.display.set_mode((500,500))
w.fill((255,255,255))
#Game Variables
game=True
x=int(round(random.randint(10,480)/10)*10)
y=int(round(random.randint(10,480)/10)*10)
x_apply=0
y_apply=0
time=pygame.time.Clock()
apple_x=int(round(random.randint(0,490)/10.0)*10.0)
apple_y=int(round(random.randint(0,490)/10.0)*10.0)
player=pygame.Rect(x,y,10,10)

score = 0
#Draw Snake Function
def draw_snake(snake_list):
    for XnY in snake_list:
        player=pygame.Rect(XnY[0],XnY[1],10,10)
        pygame.draw.rect(w,(0,0,0),player)
    pygame.display.flip() 
    
snake_L=[]
length_s=1


def button(text,color,size,pos):
         button=pygame.font.Font(None,size)
         write=button.render(text,0,color)
         w.blit(write,pos)
         
def AI_move(snake_list, apple_x, apple_y, x_shift, y_shift):

    adjust = False

    random_speed = [-10, 10]
    
    x = snake_list[-1][0]
    y = snake_list[-1][1]

    tail = snake_list[0]

    x_apply = 0
    y_apply = 0

    #Find the nearest path towards the apple.
    if x < apple_x:
        x_apply = 10
    elif x > apple_x:
        x_apply = -10

    if x == apple_x:
        if y < apple_y:
            y_apply = 10
        elif y> apple_y:
            y_apply = -10
            
    #Predict next position
    
    for i in snake_list:
        if x + x_apply == i[0] and y + y_apply == i[1]:
            adjust = True

    if adjust:
#         if (x + x_apply) == snake_list[-2][0]:
#             x_apply = 0
#             if y < tail[1]:
#                 y_apply = 10
#             elif y > tail[1]:
#                 y_apply = -10
#             else:
#                 y_apply = random.choice(random_speed)
#             
#             print(0)
#             
#         elif (y + y_apply) == snake_list[-2][1]:
#             y_apply = 0
#             if x < tail[0]:
#                 x_apply = 10
#             elif x > tail[0]:
#                 x_apply = -10
#             else:
#                 x_apply = random.choice(random_speed)
#             print(1)
            
        if x > tail[0] and x_apply == 0:
            y_apply = 0
            x_apply = -10
            print(2)
            
        elif x < tail[0] and x_apply == 0:
            y_apply = 0
            x_apply = 10
            print(3)
            
        elif y > tail[1] and y_apply == 0:
            x_apply = 0
            y_apply = -10
            print(4)
            
        elif y < tail[1] and y_apply == 0:
            x_apply = 0
            y_apply = 10
            print(5)
    
    if (-x_apply) == x_shift:
        x_apply = 0
        y_apply = random.choice(random_speed)
    
    elif (-y_apply) == y_shift:
        y_apply = 0
        x_apply = random.choice(random_speed)
            
            
    return x_apply, y_apply











while game:

    #Two main sprites, apple and snake
    apple=pygame.Rect(apple_x,apple_y,10,10)
    player=pygame.Rect(x,y,10,10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                if length_s>1:
                    if x_apply==0:
                        x_apply=10
                        y_apply=0
                else:
                    x_apply=10
                    y_apply=0
            elif event.key==pygame.K_LEFT:
                if length_s>1:
                    if x_apply==0:
                        x_apply=-10
                        y_apply=0
                else:
                    x_apply=-10
                    y_apply=0
            elif event.key==pygame.K_UP:
                if length_s>1:
                    if y_apply==0:
                        y_apply=-10
                        x_apply=0
                else:
                    y_apply=-10
                    x_apply=0
            elif event.key==pygame.K_DOWN:
                if length_s>1:
                    if y_apply==0:
                        y_apply=10
                        x_apply=0
                else:
                    y_apply=10
                    x_apply=0
        


    pygame.draw.rect(w,(0,0,255),apple)
    #Add snake position to the snake variable.
    snake_Head=[]
    snake_Head.append(x)
    snake_Head.append(y)
    snake_L.append(snake_Head)



    #Draw snake
    if len(snake_L) > length_s:
        del snake_L[0]

    draw_snake(snake_L)
    

    #AI
    x_apply, y_apply = AI_move(snake_L, apple_x, apple_y, x_apply, y_apply)
    x+=x_apply
    y+=y_apply

    #Self collide
    if snake_L[-1] in snake_L[1:-1]:
        print("GameOver")
        game=False

    if apple_x==x and apple_y==y:
        #Add 1 to the length after eating an apple
        apple_x=int(round(random.randint(0,490)/10.0)*10.0)
        #apple_y=int(round(random.randint(0,490)/10.0)*10.0)
        length_s+=1
        score += 1
    
    #Out of bond.
    if x>500:
        x-=500
    elif x<0:
        x+=500
    elif y>500:
        y-=500
    elif y<0:
        y+=500
    button(str(score), (0, 0, 0), 30, (0, 0))
    pygame.display.flip()
    w.fill((255,255,255))
    time.tick(50)

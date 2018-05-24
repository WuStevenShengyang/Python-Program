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

#Draw Snake Function
def draw_snake(snake_list):
    for XnY in snake_list:
        player=pygame.Rect(XnY[0],XnY[1],10,10)
        pygame.draw.rect(w,(0,0,0),player)
    pygame.display.flip() 
    
snake_L=[]
length_s=1

#def snake_list()
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
    
    
    x+=x_apply
    y+=y_apply
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
    #Self collide
    if snake_L[0] in snake_L[1:-1]:
        print("GameOver")
        game=False
    if apple_x==x and apple_y==y:
        #Add 1 to the length after eating an apple
        apple_x=int(round(random.randint(0,490)/10.0)*10.0)
        apple_y=int(round(random.randint(0,490)/10.0)*10.0)
        length_s+=1
    #Out of bond.
    if x>500:
        x-=500
    elif x<0:
        x+=500
    elif y>500:
        y-=500
    elif y<0:
        y+=500
    pygame.display.flip()
    w.fill((255,255,255))
    time.tick(15)

'''
Created on Dec 8, 2017

@author: s-wus
'''
import pygame

pygame.init()

w=pygame.display.set_mode((400,400))
w.fill((0,0,0))

game=True
display=0
current=pygame.time.get_ticks()

#Initial Variables
text=pygame.font.Font(None,50)
text_continue=pygame.font.Font(None,30)
font=pygame.font.Font(None,100)
zero=font.render("0.000",0,(255,255,255))
continue_text_text=text_continue.render("Continue", 0, (0,0,0))
start_text=text.render("Start",0,(0,0,0))
stop_text=text.render("Clear",0,(0,0,0))
pause_text=text.render("Pause",0,(0,0,0))
#Buttons
start=pygame.Rect(50,300,100,35)
stop=pygame.Rect(250,300,100,35)

while game:
    #Mouse position & Time Passed
    cur = pygame.mouse.get_pos()
    now = pygame.time.get_ticks()
    # Mouse moves to the rectangles
    if 50 < cur[0] < 50 + 100 and 300 < cur[1] < 300 + 35:
        R=155
    else:
        R=255

    if 250<cur[0]<250+100 and 300 < cur[1] < 300 + 35:
        G=155
    else:
        G=255

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            #Start recording
            if 50 < cur[0] < 50 + 100 and 300 < cur[1] < 300 + 35:#Mouse click START
                if display==1:#Pause timer or Start timer
                    display=2
                    text = (now - current) / 1000
                elif display==2:#continue timer
                    display=3
                    current=pygame.time.get_ticks()
                elif display==3:
                    display=2
                    text += (now - current) / 1000
                else:#Start timer
                    current=pygame.time.get_ticks()
                    display=1
            elif 250<cur[0]<250+100 and 300 < cur[1] < 300 + 35:#Mouse click STOP
                display=0#Clear timer

    pygame.draw.rect(w,(R,0,0),start)
    pygame.draw.rect(w,(0,G,0),stop)
    if display==0:#Clear timer
        w.blit(zero,(100,100))
        w.blit(start_text,(50,300))
        w.blit(stop_text,(250,300))
    elif display==1:#Start timer
        render=font.render(str((now-current)/1000),0,(255,255,255))
        w.blit(render,(100,100))
        w.blit(pause_text,(50,300))
        w.blit(stop_text,(250,300))
    elif display==2:#Pause timer
        current_text=font.render(format(text,'.3f'),0,(255,255,255))
        w.blit(current_text,(100,100))
        w.blit(stop_text,(250,300))
        w.blit(continue_text_text,(50,310))
    else:#continue timer
        continue_text=font.render(format((now-current)/1000+text,'.3f'),0,(255,255,255))
        w.blit(continue_text,(100,100))
        w.blit(stop_text,(250,300))
        w.blit(pause_text,(50,300))
        
        





    pygame.display.flip()
    w.fill((0,0,0))

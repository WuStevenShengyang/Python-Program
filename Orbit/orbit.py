import pygame
import math
pygame.init()

w=pygame.display.set_mode((1000,1000))
w.fill((0,0,0))
c=pygame.time.Clock()

earth_x=300
earth_y=500

mars_x=370
mars_y=500

jupiter_x=150
jupiter_y=500

saturn_x=100
saturn_y=500

mercury_x=450
mercury_y=500

venus_x=200
venus_x=500

sun_x=500
sun_y=400

game=True
speed=30

forward_jupiter=True
forward_venus=True
forward_mercury=True
forward_moon=True
forward_earth=True
forward_mars=True

radius_sun_jupiter=350
radius_sun_venus=300
radius_earth_moon=50
radius_sun_earth=200
radius_sun_mars=130
radius_sun_mercury=50
radius_sun_saturn=400

off_venus=0
off_moon=0
off_earth=0
off_mars=0
off_mercury=0
off_jupiter=0
off_saturn=0

background=pygame.image.load('C:/Users/s-wus/Desktop/star.png')

while game:
    #w.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                speed+=10
            elif event.key==pygame.K_DOWN:
                speed-=10

    #Moon
    circle_moon_x=earth_x-radius_earth_moon+off_moon
    
    if circle_moon_x==(earth_x+radius_earth_moon):
        forward_moon=False
    elif circle_moon_x==(earth_x-radius_earth_moon):
        forward_moon=True    
        
    if forward_moon:
        off_moon+=1
        circle_moon_y=math.sqrt(2500-(circle_moon_x-earth_x)**2)+earth_y
    else:
        off_moon-=1
        circle_moon_y=-math.sqrt(2500-(circle_moon_x-earth_x)**2)+earth_y

    pygame.draw.circle(w,(200,200,200),(circle_moon_x,int(circle_moon_y)),5,5)  
    pygame.draw.circle(w,(0,100,255),(earth_x,int(earth_y)),10,10)

    #Earth
    earth_x=sun_x-radius_sun_earth+off_earth

    if earth_x==(sun_x+290):
        forward_earth=False
    elif earth_x==(sun_x-290):
        forward_earth=True

    if forward_earth:
        off_earth+=1
        earth_y=-math.sqrt(radius_sun_earth**2-((earth_x-sun_x)**2)/2.1025)+sun_y
    else:
        off_earth-=1
        earth_y=math.sqrt(radius_sun_earth**2-((earth_x-sun_x)**2)/2.1025)+sun_y


    pygame.draw.circle(w,(255,100,0),(sun_x,sun_y),15,15)

##    #Mars
##    mars_x=sun_x-radius_sun_mars+off_mars
##
##    if mars_x==(sun_x+radius_sun_mars):
##        forward_mars=False
##    elif mars_x==(sun_x-radius_sun_mars):
##        formatward_mars=True
##
##    if forward_mars:
##        off_mars+=1
##        mars_y=math.sqrt(radius_sun_mars**2-(mars_x-sun_x)**2)+sun_y
##    else:
##        off_mars-=1
##        mars_y=-math.sqrt(radius_sun_mars**2-(mars_x-sun_x)**2)+sun_y
##
##    pygame.draw.circle(w,(150,50,0),(mars_x,int(mars_y)),7,7)


    #Mercury
    mercury_x=sun_x-radius_sun_mercury+off_mercury

    if mercury_x==(sun_x+100):
        forward_mercury=False
    elif mercury_x==(sun_x-100):
        forward_mercury=True

    if forward_mercury:
        off_mercury+=1
        mercury_y=math.sqrt(radius_sun_mercury**2-((mercury_x-sun_x)**2)/4)+sun_y
    else:
        off_mercury-=1
        mercury_y=-math.sqrt(radius_sun_mercury**2-((mercury_x-sun_x)**2)/4)+sun_y

    pygame.draw.circle(w,(100,100,100),(mercury_x,int(mercury_y)),5,5)

    #Venus
    venus_x=sun_x-radius_sun_venus+off_venus

    if venus_x==(sun_x+radius_sun_venus):
        forward_venus=False
    elif venus_x==(sun_x-radius_sun_venus):
        forward_venus=True

    if forward_venus:
        off_venus+=1
        venus_y=math.sqrt(radius_sun_venus**2-(venus_x-sun_x)**2)+sun_y
    else:
        off_venus-=1
        venus_y=-math.sqrt(radius_sun_venus**2-(venus_x-sun_x)**2)+sun_y

    pygame.draw.circle(w,(150,150,30),(venus_x,int(venus_y)),11,11)

    #Jupiter
    jupiter_x=sun_x-radius_sun_jupiter+off_jupiter

    if jupiter_x==(sun_x+radius_sun_jupiter):
        forward_jupiter=False
    elif jupiter_x==(sun_x-radius_sun_jupiter):
        forward_jupiter=True

    if forward_jupiter:
        off_jupiter+=1
        jupiter_y=math.sqrt(radius_sun_jupiter**2-(jupiter_x-sun_x)**2)+sun_y
    else:
        off_jupiter-=1
        jupiter_y=-math.sqrt(radius_sun_jupiter**2-(jupiter_x-sun_x)**2)+sun_y

    pygame.draw.circle(w,(249,205,104),(jupiter_x,int(jupiter_y)),18,18)

    #Saturn
    saturn_x=sun_x-radius_sun_saturn+off_saturn

    if saturn_x==(sun_x+radius_sun_saturn):
        forward_saturn=False
    elif saturn_x==(sun_x-radius_sun_saturn):
        forward_saturn=True

    if forward_saturn:
        off_saturn+=1
        saturn_y=math.sqrt(radius_sun_saturn**2-(saturn_x-sun_x)**2)+sun_y
    else:
        off_saturn-=1
        saturn_y=-math.sqrt(radius_sun_saturn**2-(saturn_x-sun_x)**2)+sun_y
        
    saturn_ring=pygame.Rect(saturn_x-25,saturn_y-5,50,10)
    pygame.draw.ellipse(w,(255,244,98),saturn_ring)
    pygame.draw.circle(w,(223,212,57),(saturn_x,int(saturn_y)),15,15)    

    #c.tick(speed)
    pygame.display.flip()
    w.fill((0,0,0))

import pygame
import random
import sys

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

w=pygame.display.set_mode((600,600))
w.fill((255,255,255))

clock=pygame.time.Clock()
#button=pygame.font.Font(None,100)
#smallFont=pygame.font.Font(None,30)

def button(text,color,size,pos):
         button=pygame.font.Font(None,size)
         write=button.render(text,0,color)
         w.blit(write,pos)
        
def setup():
         R=255
         G=200
         game=True
         while game:
                  cur=pygame.mouse.get_pos()
                  for event in pygame.event.get():
                           if event.type==pygame.QUIT:
                                    game=False
                           if event.type==pygame.MOUSEBUTTONDOWN:
                                    if 100<cur[0]<260 and 400<cur[1]<480:
                                             game=False
                                    elif 400<cur[0]<560 and 400<cur[1]<480:
                                             pygame.quit()
                                             quit()
                                             
                  if 100<cur[0]<260 and 400<cur[1]<480:
                           R=215
                  else:
                           R=255

                  if 400<cur[0]<560 and 400<cur[1]<480:
                           G=150
                  else:
                           G=200
                           
                  red_rect=pygame.Rect(100,400,160,80)
                  yellow_rect=pygame.Rect(400,400,160,80)
                  
                  #red=button.render("Start",0,(0,0,0))
                  #yellow=button.render("Quit",0,(0,0,0))
                  
                  pygame.draw.rect(w,(R,0,0),red_rect)
                  pygame.draw.rect(w,(200,G,0),yellow_rect)

                  button("Start",(0,0,0),100,(100,400))
                  button("Quit",(0,0,0),100,(400,400))
                  button("T   A   N   K",(50,50,50),150,(30,65))
                  button("Control by ARROWS, press SPACE to fire, use A and D to adjust power.",(0,150,0),25,(10,200))
                  
                  #w.blit(red,(100,400))
                  #w.blit(yellow,(400,400))
                  
                  pygame.display.flip()
                  w.fill((255,255,255))

def gameover():
         R=255
         G=200
         game=True
         while game:
                  cur=pygame.mouse.get_pos()
                  for event in pygame.event.get():
                           if event.type==pygame.QUIT:
                                    game=False
                           if event.type==pygame.MOUSEBUTTONDOWN:
                                    if 100<cur[0]<260 and 400<cur[1]<480:
                                             main()
                                    elif 400<cur[0]<560 and 400<cur[1]<480:
                                             pygame.quit()
                                             quit()
                                             
                  if 100<cur[0]<260 and 400<cur[1]<480:
                           R=215
                  else:
                           R=255

                  if 400<cur[0]<560 and 400<cur[1]<480:
                           G=150
                  else:
                           G=200
                           
                  red_rect=pygame.Rect(100,400,250,80)
                  yellow_rect=pygame.Rect(400,400,160,80)
                  
                  
                  
                  pygame.draw.rect(w,(R,0,0),red_rect)
                  pygame.draw.rect(w,(200,G,0),yellow_rect)

                  
                  button("Play Again",(0,0,0),70,(100,410))
                  button("Quit",(0,0,0),100,(400,400))
                  button("Game Over",(0,0,0),100,(125,50))
                  button("You Died!",(255,0,0),30,(225,150))
                  #w.blit(red,(100,400))
                  #w.blit(yellow,(400,400))
                  
                  pygame.display.flip()
                  w.fill((255,255,255))
                  
def game_win():
         R=255
         G=200
         game=True
         while game:
                  cur=pygame.mouse.get_pos()
                  for event in pygame.event.get():
                           if event.type==pygame.QUIT:
                                    game=False
                           if event.type==pygame.MOUSEBUTTONDOWN:
                                    if 100<cur[0]<260 and 400<cur[1]<480:
                                             main()
                                    elif 400<cur[0]<560 and 400<cur[1]<480:
                                             pygame.quit()
                                             quit()
                                             
                  if 100<cur[0]<260 and 400<cur[1]<480:
                           R=215
                  else:
                           R=255

                  if 400<cur[0]<560 and 400<cur[1]<480:
                           G=150
                  else:
                           G=200
                           
                  red_rect=pygame.Rect(100,400,250,80)
                  yellow_rect=pygame.Rect(400,400,160,80)
                  
                  
                  
                  pygame.draw.rect(w,(R,0,0),red_rect)
                  pygame.draw.rect(w,(200,G,0),yellow_rect)

                  button("Play Again",(0,0,0),70,(100,410))
                  button("Quit",(0,0,0),100,(400,400))
                  button("You WON!",(0,180,0),100,(120,50))
                  #w.blit(red,(100,400))
                  #w.blit(yellow,(400,400))
                  
                  pygame.display.flip()
                  w.fill((255,255,255))


def tank(tankx,tanky,index,turret_pos):
         #Draw Tank                  
         pygame.draw.circle(w,(0,0,0),(tankx,tanky),14,14)
         pygame.draw.rect(w,(0,0,0),[tankx-20,tanky,40,15])
         pygame.draw.line(w,(0,0,0),(tankx,tanky),turret_pos[index],7)
         #else:
         #pygame.draw.line(w,(0,0,0),(520+offset,540),turret_coor_R[index],7) 
         pygame.draw.circle(w,(0,0,0),(tankx+25-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+30-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+35-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+40-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+45-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+50-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+55-40,tanky+15),5,5)
         #Draw wall

def enemy_tank(tankx,tanky,index,turret_pos):
         #Draw Tank                  
         pygame.draw.circle(w,(0,0,0),(tankx,tanky),14,14)
         pygame.draw.rect(w,(0,0,0),[tankx-20,tanky,40,15])
         pygame.draw.line(w,(0,0,0),(tankx,tanky),turret_pos[index],7)
         #else:
         #pygame.draw.line(w,(0,0,0),(520+offset,540),turret_coor_R[index],7) 
         pygame.draw.circle(w,(0,0,0),(tankx+25-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+30-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+35-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+40-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+45-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+50-40,tanky+15),5,5)
         pygame.draw.circle(w,(0,0,0),(tankx+55-40,tanky+15),5,5)
         #Draw wall

def main():
         game=True
         
         speed=0
         
         index=0
         
         fire=False
         
         xlocation_wall=random.randint(300-0.1*600,300+0.1*600)
         height=random.randint(0.1*600,0.4*600)

         powerOrigin=7
         powerChange=0

         tankx=int(0.9*600)
         tanky=int(0.9*600)

         enemyx=int(0.1*600)
         enemyy=int(0.9*600)
         enemy_move=0
         enemy_speed=1
         
         player_health=100
         enemy_health=100

         p_damage=0
         e_damage=0
         
         while game:
                  turret_coor_self=[(tankx-36,tanky-4),
                                    (tankx-34,tanky-6),
                                    (tankx-32,tanky-8),
                                    (tankx-30,tanky-10),
                                    (tankx-28,tanky-12),
                                    (tankx-26,tanky-14),
                                    (tankx-24,tanky-16),
                                    (tankx-22,tanky-18),
                                    (tankx-20,tanky-20),
                                    (tankx-18,tanky-22),
                                    (tankx-16,tanky-24),
                                    (tankx-14,tanky-26),
                                    ]

                  turret_coor_enemy=[(enemyx+36,enemyy-4),
                                    (enemyx+34,enemyy-6),
                                    (enemyx+32,enemyy-8),
                                    (enemyx+30,enemyy-10),
                                    (enemyx+28,enemyy-12),
                                    (enemyx+26,enemyy-14),
                                    (enemyx+24,enemyy-16),
                                    (enemyx+22,enemyy-18),
                                    (enemyx+20,enemyy-20),
                                    (enemyx+18,enemyy-22),
                                    (enemyx+16,enemyy-24),
                                    (enemyx+14,enemyy-26),
                                    ]

                  #turret_coor=[(479+offset,530),(481+offset,528),(483+offset,526),(485+offset,524),(487+offset,522),(490+offset,520),(493+offset,518),(495+offset,516),(497+offset,514),(499+offset,512),(501+offset,510),(503+offset,508)]
                  #turret_coor_R=[(479+offset+82,530),(481+offset+78,528),(483+offset+74,526),(485+offset+70,524),(487+offset+66,522),(490+offset+62,520),(493+offset+58,518),(495+offset+54,516)]
         
                  #Out of bond
                  if tankx-20<xlocation_wall+50:
                           tankx+=1
                  elif tankx+20>600:
                           tankx-=1
                  #max and min power:
                  powerOrigin+=powerChange
                  if powerOrigin>=100:
                           powerOrigin=100
                  elif powerOrigin<=0:
                           powerOrigin=1
                  powerDisplay(powerOrigin)
                  #Draw wall
                  wall(xlocation_wall,height,50)
                  #Draw Ground
                  draw_ground()
                  #Move Tank
                  tankx+=speed
                  clock.tick(90)
                  #Move enemy tank
                  if enemyx<=20:
                           enemy_speed=1
                  elif enemyx>xlocation_wall-30:
                           enemy_speed=-1
                  enemyx+=enemy_speed
                  #Drawv health bar
                  health(player_health,enemy_health)
                  #Draw tank
                  tank(tankx,tanky,index,turret_coor_self)

                  #Draw enemy tank
                  enemy_tank(enemyx,enemyy,9,turret_coor_enemy)
                  #Damage display
                  damage_display(p_damage,e_damage)
                  #Game Over, victory
                  if player_health<=0:
                           gameover()
                           game=False
                  elif enemy_health<=0:
                           game_win()
                           game=False
                           
                  for event in pygame.event.get():
                           if event.type==pygame.QUIT:
                                    game=False
                           if event.type==pygame.KEYDOWN:
                                    if event.key==pygame.K_RIGHT:
                                             speed=1
                                    elif event.key==pygame.K_LEFT:
                                             speed=-1
                                    elif event.key==pygame.K_UP:
                                             index+=1
                                             if index>=len(turret_coor_self)-1:
                                                      index=len(turret_coor_self)-1
                                    elif event.key==pygame.K_DOWN:
                                             index-=1
                                             if index<=0:
                                                      index=0
                                    elif event.key==pygame.K_SPACE:
                                             p_damage=fireS(turret_coor_self[index],index,powerOrigin,xlocation_wall,height,50,1,enemyx,0,0)
                                             e_damage=e_fireS(turret_coor_enemy[10],10,xlocation_wall,height,50,tankx)

                                             player_health-=e_damage
                                             enemy_health-=p_damage
                                             
                                    elif event.key==pygame.K_d:
                                             powerChange=1
                                    elif event.key==pygame.K_a:
                                             powerChange=-1
                           
                           if event.type==pygame.KEYUP:
                                    if event.key==pygame.K_RIGHT:
                                             speed=0
                                    elif event.key==pygame.K_LEFT:
                                             speed=0
                                    elif event.key==pygame.K_d or event.key==pygame.K_a:
                                             powerChange=0
                                    
                  pygame.display.flip()
                  w.fill((255,255,255))

def damage_display(player_damage,enemy_damage):
         button("Player damage taken:"+str(enemy_damage),(0,0,0),30,(360,70))
         button("Enemy damage taken:"+str(player_damage),(0,0,0),30,(20,70))
         
def wall(x,height,width):
         pygame.draw.rect(w,(0,0,0),[x,(600-height),width,height])

def draw_ground():
         pygame.draw.rect(w,(0,180,0),[0,560,600,40])

def health(player_health,enemy_health):
         if player_health>75:
                  player_health_color=(0,200,0)
         elif player_health>50:
                  player_health_color=(255,100,0)
         else:
                  player_health_color=(255,0,0)

         if enemy_health>75:
                  enemy_health_color=(0,200,0)
         elif enemy_health>50:
                  enemy_health_color=(255,100,0)
         else:
                  enemy_health_color=(255,0,0)

         pygame.draw.rect(w,player_health_color,[480,30,player_health,20])
         pygame.draw.rect(w,enemy_health_color,[20,30,enemy_health,20])
         button(str(player_health)+"%",player_health_color,30,(480,50))
         button(str(enemy_health)+"%",enemy_health_color,30,(20,50))
         
def fireS(coor,index,powerlevel,wall_x,wall_y,width,np,enemyx,true_power,shoot_power):
         damage=0
         fire=True
         xy=list(coor)
         while fire:
                  for event in pygame.event.get():
                           if event.type==pygame.QUIT:
                                    pygame.quit()
                                    quit()
                  pygame.draw.circle(w,(255,0,0),(xy[0],xy[1]),5,5)
                  xy[0]-=(12-index)*2*np
                  xy[1]+=int(((xy[0]-coor[0])*0.015/(powerlevel/100))**2-8)

                  check_x_1 = xy[0] <= (wall_x+width)
                  check_x_2 = xy[0] >= wall_x
                  check_y = xy[1] >= (600-wall_y)
                  
                  if xy[1]>560:
                           if enemyx-35<xy[0]<enemyx+35:
                                    #Amount of damage
                                    if enemyx==xy[0]:
                                             damage=50
                                    elif enemyx-25<xy[0]<enemyx+25:
                                             damage=25
                                    else:
                                             damage=15
                                    
                           hit_x=int(xy[0]*600/xy[1])
                           hit_y=600
                           explosion(hit_x,hit_y-40)
                           fire=False
                           
                  elif int(0.85*true_power)<shoot_power<int(1.5*true_power):
                           #Amount of damage
                           if int(true_power)==shoot_power:
                                    damage=50
                           elif int(0.9*true_power)<shoot_power<int(1.1*true_power):
                                    damage=25
                           elif int(0.85*true_power)<shoot_power<int(1.15*true_power):
                                    damage=15
                  if check_x_1 and check_x_2 and check_y:
                           fire=False
                           explosion(xy[0],xy[1])
                           damage=0
                  else:
                           pass
                                    
                  pygame.display.update()
                  clock.tick(40)
         #print("Player damage",damage)
         return damage

def e_fireS(coor,index,wall_x,wall_y,width,tankx):
         fire=True
         xy=list(coor)
         damage=0
         found=False
         true_power=1
         while not found:

                  fire=True
                  xy=list(coor)
                  while fire:
                           for event in pygame.event.get():
                                    
                                    if event.type==pygame.QUIT:
                                             pygame.quit()
                                             quit()
                           xy[0]+=(12-index)*2
                           xy[1]+=int(((xy[0]-coor[0])*0.015/(true_power/100))**2-8)
                           #pygame.draw.circle(w,(255,0,0),(xy[0],xy[1]),5)
                           #check_x_1 = xy[0] <= (wall_x+width)
                           #check_x_2 = xy[0] >= wall_x
                           #check_y = xy[1] >= (600-wall_y)
                           
                           #if check_x_1 and check_x_2 and check_y:
                                    #fire=False
                                    #explosion(xy[0],xy[1])
                           
                           if xy[1]>560:
                                    hit_x=int(xy[0]*600/xy[1])
                                   
                                    if hit_x>=tankx:
                                             found=True
                                             shoot_power=random.randint(int(0.85*true_power),int(1.2*true_power))

                                             """if int(0.85*true_power)<shoot_power<int(1.5*true_power):
                                                      #Amount of damage
                                                      if int(true_power)==shoot_power:
                                                               damage=50
                                                      elif int(0.9*true_power)<shoot_power<int(1.1*true_power):
                                                               damage=25
                                                      elif int(0.85*true_power)<shoot_power<int(1.15*true_power):
                                                               damage=15"""
                                             
                                             damage=fireS(coor,index,shoot_power,wall_x,wall_y,50,-1,0,true_power,shoot_power)
                                    fire=False
                           pygame.display.update()
                  true_power+=1
         return damage
                  
def explosion(x,y):
         magnitude=1
         color=[(255,0,0),(255,100,0),(200,200,0),(150,180,0)]
         while magnitude<50:
                  explosion_x=x+random.randint(-1*magnitude,magnitude)
                  explosion_y=y+random.randint(-1*magnitude,magnitude)
                  pygame.draw.circle(w,(color[random.randint(0,3)]),(explosion_x,explosion_y),random.randint(1,5))
                  pygame.display.flip()
                  magnitude+=2
                  clock.tick(35)
                  
                  

def powerDisplay(level):
         
         button("Power:"+str(level)+"%",(0,0,0),35,(300,20))
         #level=smallFont.render("Power:"+str(level)+"%",0,(0,0,0))
         #w.blit(level,[300,20])
   
setup()  
main()

         




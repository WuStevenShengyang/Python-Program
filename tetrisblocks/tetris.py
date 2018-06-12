from sprite import *
import pygame
import random
from tkinter.constants import CURRENT

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH = 288
HEIGHT = 480

w = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Tetris')
w.fill(BLACK)

c = pygame.time.Clock()

long = [
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/long/long_original.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/long/long_90.png'
    ]

square = [
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/square/square.png'
    ]

three_one = [
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/three_one/three_one_original.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/three_one/three_one_90.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/three_one/three_one_180.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/three_one/three_one_270.png'
    ]

right_zig = [
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/right_zig/right_zig_original.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/right_zig/right_zig_90.png'
    ]

left_zig = [
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/left_zig/left_zig_original.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/left_zig/left_zig_90.png'
    ]

right_turn = [
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/right_turn/right_turn_original.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/right_turn/right_turn_90.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/right_turn/right_turn_180.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/right_turn/right_turn_270.png'
    ]

left_turn = [
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/left_turn/left_turn_original.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/left_turn/left_turn_90.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/left_turn/left_turn_180.png',
    'C:/Users/s-wus/Desktop/tetrisblocks/resource/left_turn/left_turn_270.png'
    ]

blocks = [long, square, three_one, right_zig, left_zig, right_turn, left_turn]

def gravity(sprite):
    sprite.center_y += 24


def move_block(sprite, speed):
    sprite.center_x += speed

def main():
    FRAME = 3
    
    game = True
    
    shape_total = []
    
    index = 0
    
    current_list = random.choice(blocks)
    current_block = sprite.Sprite(current_list[0], 120, 0)
    shape_total.append(current_block)
    
    wall = sprite.Sprite('C:/Users/s-wus/Desktop/tetrisblocks/resource/black.jpg', 0, 479)
    wall.scale = 2
    
    while game:
        #Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    index += 1
                    if index == 4:
                        index = 0
                    
                    current_block.image(current_list[index])
                   
                #Move Left & Right
                elif event.key == pygame.K_RIGHT:
                    current_block.center_x += 24
                elif event.key == pygame.K_LEFT:
                    current_block.center_x -= 24

                #Increase falling speed
                elif event.key == pygame.K_DOWN:
                    FRAME = 15
                    
            #Reset frame
            elif event.type == pygame.KEYUP:
                FRAME = 3
                
        #Move block
        gravity(current_block)
        for shapes in shape_total:
            shapes.draw()

        #Collide with ground
        if pygame.sprite.collide_rect(current_block, wall):
            index = 0
            current_block = sprite.Sprite(random.choice(blocks)[0], 120, 0)
            shape_total.append(current_block)

        pygame.display.flip()
        w.fill(BLACK)
        c.tick(FRAME)


if __name__ == '__main__':
    main()

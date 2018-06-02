import random
import pygame
from pygame.examples.testsprite import Static

pygame.init()
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]

class Snake(pygame.sprite.Sprite):
    def __init__(self, width, height):
        self.snake_length = 1
        self.snake_list = []
        
        self.width = width
        self.height = height
        
        self.score = 0
        
        self.x = round(random.randint(0, self.width - 10)/10)*10
        self.y = round(random.randint(0, self.height - 10)/10)*10
        
        self.snake_head = pygame.Rect(self.x, self.y, 10, 10)
        self.snake_list.append(self.snake_head)
        
        self.surface = pygame.display.get_surface()
    
    def move_snake(self, x_speed, y_speed):
        self.snake_head.x += x_speed
        self.snake_head.y += y_speed
        
    def draw_snake(self):
        for snake in self.snake_list:
            pygame.draw.rect(self.surface, BLACK, snake)
    
    def generate_food(self):
        self.apple_x = round(random.randint(0, self.width - 10)/10)*10
        self.apple_y = round(random.randint(0, self.height - 10)/10)*10
        
        self.apple = pygame.Rect(self.apple_x, self.apple_y, 10, 10)
        
    def draw_food(self):
        pygame.draw.rect(self.surface, RED, self.apple)
    
    def eat_food(self):
        if self.apple_x == self.snake_head.x and self.apple_y == self.snake_head.y:
            self.score += 1
            self.snake_length += 30
            self.generate_food()
    
        
    def increase_length(self):
        body = (self.snake_head[0], self.snake_head[1])
        rect = pygame.Rect(body[0], body[1], 10, 10)
        self.snake_list.append(rect)
        
        if len(self.snake_list) > self.snake_length:
            self.snake_list.remove(self.snake_list[0])
           
    def self_collide(self):
        for snake in self.snake_list[1:-1]:
            if snake.colliderect(self.snake_head):
                pygame.quit()
     
    def AI(self):
        pass 
        
def main():
    #Initialize Window
    width = 250
    height = 250
    w = pygame.display.set_mode([width, height])
    w.fill(WHITE)
    
    #Snake Speed
    x_speed = 0
    y_speed = 0
    
    snake = Snake(width, height)
    snake.generate_food()
   
    game = True
    c = pygame.time.Clock()
    
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_speed = -10
                    x_speed = 0
                elif event.key == pygame.K_DOWN:
                    y_speed = 10
                    x_speed = 0
                elif event.key == pygame.K_LEFT:
                    x_speed = -10
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = 10
                    y_speed = 0
                   
        snake.move_snake(x_speed, y_speed) 
        snake.draw_snake()
        
        snake.draw_food()
        snake.eat_food()
        
        snake.self_collide()
        snake.increase_length()
        
        pygame.display.flip()
        w.fill(WHITE)
        c.tick(30)
    
   
if __name__ == "__main__":
    main()
   
    
    
    
    
    
    
    
      

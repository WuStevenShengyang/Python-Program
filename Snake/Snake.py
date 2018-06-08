import random
import pygame
import math

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]

class Snake(pygame.sprite.Sprite):

    def __init__(self, width, height, *groups):
        super().__init__(*groups)
        self.snake_length = 10
        self.snake_list = []
        
        self.width = width
        self.height = height
        
        self.score = 0
        
        self.x = round(random.randint(0, self.width - 10)/10)*10
        self.y = round(random.randint(0, self.height - 10)/10)*10
        
        self.snake_head = pygame.Rect(self.x, self.y, 10, 10)
        self.snake_list.append(self.snake_head)
        
        self.surface = pygame.display.get_surface()

        self.x_speed = 0
        self.y_speed = 0

        self.apple_x = 0
        self.apple_y = 0

    def move_snake(self, x_speed, y_speed):
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.snake_head.x += x_speed
        self.snake_head.y += y_speed
        
    def draw_snake(self):
        for snake in self.snake_list:
            pygame.draw.rect(self.surface, BLACK, snake)
    
    def generate_food(self):
        self.apple_x = round(random.randint(0, self.width - 10)/10)*10
        self.apple_y = round(random.randint(0, self.height - 10)/10)*10

        self.apple = pygame.Rect(self.apple_x, self.apple_y, 10, 10)

        for snake in self.snake_list:
            if snake.colliderect(self.apple):
                self.generate_food()
        
    def draw_food(self):
        pygame.draw.rect(self.surface, RED, self.apple)
    
    def eat_food(self):
        if self.apple_x == self.snake_head.x and self.apple_y == self.snake_head.y:
            self.score += 1
            self.snake_length += 1
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
                return True
     
    def AI(self): #<--------------------------------------- Big Bang
        x_speed = 0
        y_speed = 0

        random_speed = [10, -10]

        if self.snake_head.x < self.apple_x:
            x_speed = 10

        elif self.snake_head.x > self.apple_x:
            x_speed = -10

        elif self.snake_head.x == self.apple_x:
            if self.snake_head.y < self.apple_y:
                y_speed = 10
            elif self.snake_head.y > self.apple_y:
                y_speed = -10

        if -(x_speed) == self.x_speed and x_speed != 0:
            x_speed = 0

            if self.snake_head.y < self.apple_y:
                y_speed = 10
            elif self.snake_head.y > self.apple_y:
                y_speed = -10
            else:
                y_speed = random.choice(random_speed)

        elif -(y_speed) == self.y_speed and y_speed != 0:
            y_speed = 0

            if self.snake_head.x < self.apple_x:
                x_speed = 10
            elif self.snake_head.y > self.apple_x:
                x_speed = -10
            else:
                x_speed = random.choice(random_speed)



        return x_speed, y_speed

    def follow_tail(self):
        x_speed = 0
        y_speed = 0

        tail = self.snake_list[0]

        dx, dy = tail[0] - self.snake_head.x, tail[1] - self.snake_head.y


        dist = math.hypot(dx, dy)


        dx /= dist
        dx = 0

        dy /= dist
        dy = 0

        if dx > 0:
            x_speed = 10
        elif dx < 0:
            x_speed = -10

        if dy > 0:
            y_speed = 10
        elif dy < 0:
            y_speed = -10

        return x_speed, y_speed




def main():

    pygame.init()
#   Initialize Window
    width = 250
    height = 250
    w = pygame.display.set_mode([width, height])
    w.fill(WHITE)
    
#   Snake Speed
    x_speed = 10
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

#       Determine speed with AI
        x_speed, y_speed = snake.AI()

#       Move snake with vertical speed 'y_speed' & horizontal speed 'x_speed'
        snake.move_snake(x_speed, y_speed) 
        snake.draw_snake()

#       Utilize apple
        snake.draw_food()
        snake.eat_food()

#       Check self collide

        if snake.self_collide():
            game = False

#       Increase length if applicable
        snake.increase_length()
        
        pygame.display.flip()
        w.fill(WHITE)
        c.tick(30)
    
   
if __name__ == "__main__":
    main()
   
    
    
    
    
    
    
    


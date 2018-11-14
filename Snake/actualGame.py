import random
import pygame
pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    snake_x = round(random.randint(0, 290)/10)*10
    snake_y = round(random.randint(0, 290)/10)*10
    
    speed_x = 0
    speed_y = 0
    
    w = pygame.display.set_mode([300, 300])
    w.fill(WHITE)
    
    snake_head = pygame.Rect(snake_x, snake_y, 10, 10)
    snake_list = []
    snake_list.append(snake_head)
    
    game = True
    
    clock = pygame.time.Clock()
    
    length = 0
    
    apple_x = round(random.randint(0, 290)/10)*10
    apple_y = round(random.randint(0, 290)/10)*10
    apple = pygame.Rect(apple_x, apple_y, 10, 10)
    
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed_x = 0
                    speed_y = -10
                elif event.key == pygame.K_DOWN:
                    speed_x = 0
                    speed_y = 10
                elif event.key == pygame.K_RIGHT:
                    speed_x = 10
                    speed_y = 0
                elif event.key == pygame.K_LEFT:
                    speed_x =-10
                    speed_y = 0
        
        
        
        
        snake_head.x += speed_x
        snake_head.y += speed_y
        
        if snake_head.x > 300:
            snake_head.x = -10
        elif snake_head.x < 0:
            snake_head.x = 300
        
        if snake_head.y > 300:
            snake_head.y = -10
        elif snake_head.y < 0:
            snake_head.y = 300
        
        if snake_head.colliderect(apple):
            length += 1
            apple_x = round(random.randint(0, 290)/10)*10
            apple_y = round(random.randint(0, 290)/10)*10
            apple = pygame.Rect(apple_x, apple_y, 10, 10)
     
                
        for snake in snake_list:      
            pygame.draw.rect(w, BLACK, snake)
        
        if len(snake_list) > length:
            print(snake_list)
            snake_list.remove(snake_list[0])
        
        body = (snake_head[0], snake_head[1])
        rect = pygame.Rect(body[0], body[1], 10, 10)
        snake_list.append(rect)
        
        for snake in snake_list[1:-1]:
            if snake_head.colliderect(snake):
                game = False
      
    
        
        pygame.draw.rect(w, RED, apple)
                
        clock.tick(20)
        pygame.display.flip()
        w.fill(WHITE)
                
if __name__ == "__main__":
    main();


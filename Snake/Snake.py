import random
import pygame
import math

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]


class Snake(pygame.sprite.Sprite):

    ### Constructor #####################################
    def __init__(self, width, height, *groups):
        super().__init__(*groups)
        # Snake List
        self.snake_length = 1
        self.snake_list = []

        # Screen Size
        self.width = width
        self.height = height

        self.score = 0

        self.x = round(random.randint(0, self.width - 10) / 10) * 10
        self.y = round(random.randint(0, self.height - 10) / 10) * 10

        self.snake_head = pygame.Rect(self.x, self.y, 10, 10)
        self.snake_list.append(self.snake_head)
        self.path = []
        self.index = 0

        self.surface = pygame.display.get_surface()

        self.x_speed = 0
        self.y_speed = 0

        self.apple_x = 0
        self.apple_y = 0

    ### Moving Functions ################################
    def move_snake(self, x_speed, y_speed):
        self.x_speed = x_speed
        self.y_speed = y_speed

        self.snake_head.x += x_speed
        self.snake_head.y += y_speed

    def path_move_snake(self):
        if self.path[self.index] == 1:
            x_speed = 10
            y_speed = 0
        elif self.path[self.index] == 2:
            x_speed = -10
            y_speed = 0
        elif self.path[self.index] == 3:
            y_speed = 10
            x_speed = 0
        elif self.path[self.index] == 4:
            y_speed = -10
            x_speed = 0

        self.index += 1
        self.snake_head.x += x_speed
        self.snake_head.y += y_speed

    def draw_snake(self):
        for snake in self.snake_list:
            pygame.draw.rect(self.surface, BLACK, snake)

    ### Apple Functions ##################################
    def generate_food(self):
        self.apple_x = round(random.randint(0, self.width - 10) / 10) * 10
        self.apple_y = round(random.randint(0, self.height - 10) / 10) * 10

        self.apple = pygame.Rect(self.apple_x, self.apple_y, 10, 10)

        for snake in self.snake_list:
            if snake.colliderect(self.apple):
                self.generate_food()

    def draw_food(self):
        pygame.draw.rect(self.surface, RED, self.apple)

    def eat_food(self):
        if self.apple.colliderect(self.snake_head):
            self.path = []
            self.index = 0
            self.score += 1
            self.snake_length += 1
            self.generate_food()

            return True
        else:
            return False

    ### Self Issues #####################################
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

    ### AI Functions (Under construction) ##############################
    def path_finder(self):
        found = False

        dx, dy = self.apple_x - self.snake_head.x, self.apple_y - self.snake_head.y
        dist = math.hypot(dx, dy)

        mock_snake = pygame.Rect(self.snake_head.x, self.snake_head.y, 10, 10)

        try:
            dx /= dist
        except Exception:
            dx = 0
        try:
            dy /= dist
        except Exception:
            dy = 0
        while not found:
            if mock_snake.x == self.apple_x and mock_snake.y == self.apple_y:
                found = True

            else:
                # print(self.path)
                # print('--------------------------')
                # print(mock_snake.x, mock_snake.y)
                # print(self.apple_x, self.apple_y)

                if mock_snake.x != self.apple_x:
                    if dx > 0:
                        mock_snake.x += 10
                        self.path.append(1)

                        while mock_snake in self.snake_list[1: -1]:
                            self.path.remove(self.path[-1])
                            self.path.append(random.choice([2, 3, 4]))

                    elif dx < 0:
                        mock_snake.x += -10
                        self.path.append(2)

                        while mock_snake in self.snake_list[1: -1]:
                            self.path.remove(self.path[-1])
                            self.path.append(random.choice([1, 3, 4]))


                else:

                    if dy > 0:
                        mock_snake.y += 10
                        self.path.append(3)

                        while mock_snake in self.snake_list[1: -1]:
                            self.path.remove(self.path[-1])
                            self.path.append(random.choice([1, 2, 4]))

                    elif dy < 0:
                        mock_snake.y += -10
                        self.path.append(4)

                        while mock_snake in self.snake_list[1: -1]:
                            self.path.remove(self.path[-1])
                            self.path.append(random.choice([1, 3, 2]))

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
    snake.path_finder()
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
        snake.path_move_snake()
        #       Draw Snake
        snake.draw_snake()

        #       Utilize apple
        snake.draw_food()
        if snake.eat_food():
            snake.path_finder()

        #       Check self collide

        # if snake.self_collide():
        # game = False

        #       Increase length if applicable
        snake.increase_length()

        pygame.display.flip()
        w.fill(WHITE)
        c.tick(30)


if __name__ == "__main__":
    main()
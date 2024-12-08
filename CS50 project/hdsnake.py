import pygame, sys, random
from pygame.math import Vector2

pygame.display.set_caption('PACSNAKE')
#PAC-MAN(TM) of 1980 Bandai Namco, images pulled from free png websites
#Duck used to aid in general help, troubleshooting errors, and condensing code
#ChatGPT used to help create snake mechanics, scoring, and collision code
#Built and run in VS CODE - would not run pygame in CS50 Codespace (copied into CS50 for submisison)

#Making the snake using PAC-MAN *.png files
class PACSNAKE:
    def __init__(self):
        self.body = [Vector2(10,11), Vector2(9,11), Vector2(8,11)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_images = {
            "up": pygame.image.load('CS50 project/Graphics/pac_up.png').convert_alpha(),
            "down": pygame.image.load('CS50 project/Graphics/pac_down.png').convert_alpha(),
            "right": pygame.image.load('CS50 project/Graphics/pac_right.png').convert_alpha(),
            "left": pygame.image.load('CS50 project/Graphics/pac_left.png').convert_alpha()
        }
        self.body_image = pygame.image.load('CS50 project/Graphics/pac_body.png').convert_alpha()
        self.eat_sound = pygame.mixer.Sound('CS50 project/Sound/pacman_eatghost.wav')
        self.intro_sound = pygame.mixer.Sound('CS50 project/Sound/pacman_beginning.wav')
        self.death_sound = pygame.mixer.Sound('CS50 project/Sound/pacman_death.wav')

    def draw_snake(self):
        self.update_head_graphics()
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            else:
                screen.blit(self.body_image, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_images["left"]
        elif head_relation == Vector2(-1,0): self.head = self.head_images["right"]
        elif head_relation == Vector2(0,1): self.head = self.head_images["up"]
        elif head_relation == Vector2(0,-1): self.head = self.head_images["down"]

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_eat_sound(self):
        self.eat_sound.play()
    def play_intro_sound(self):
        self.intro_sound.play()
    def play_death_sound(self):
        self.death_sound.play()

    def reset(self):
        self.body = [Vector2(10,11), Vector2(9,11), Vector2(8,11)]
        self.direction = Vector2(1,0)
#Creating the 3 Ghosts
class GHOST:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.randomize()

    def draw_ghost(self):
        ghost_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(self.image, ghost_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
#Main mechanics and collisions
class MAIN:
    def __init__(self):
        self.snake = PACSNAKE()
        self.ghosts = [GHOST('CS50 project/Graphics/ghost.png'), GHOST('CS50 project/Graphics/ghost2.png'), GHOST('CS50 project/Graphics/ghost3.png')]

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        for ghost in self.ghosts:
            ghost.draw_ghost()
        self.snake.draw_snake()
        self.draw_score()
#chatgpt help
    def check_collision(self):
        for ghost in self.ghosts:
            if ghost.pos == self.snake.body[0]:
                ghost.randomize()
                self.snake.add_block()
                self.snake.play_eat_sound()
        for block in self.snake.body[1:]:
            for ghost in self.ghosts:
                if block == ghost.pos:
                    ghost.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.snake.play_death_sound()
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.snake.play_death_sound()
                self.game_over()

    def game_over(self):
        self.snake.reset()
        global game_started
        game_started = False
#scoring - chatgpt help
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (200,74,12))
        score_x = 70
        score_y = 375
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        blink_rect = blink.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(blink_rect.left, blink_rect.top, blink_rect.width + score_rect.width + 6, blink_rect.height)

        pygame.draw.rect(screen, (0,0,61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(blink, blink_rect)
        pygame.draw.rect(screen, (50,50,50), bg_rect, 2)
#chat gpt help with game board setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
blink = pygame.image.load('CS50 project/Graphics/ghost.png').convert_alpha()
game_font = pygame.font.Font('CS50 project/Font/PoetsenOne-Regular.ttf', 25)
background_image = pygame.image.load('CS50 project/Graphics/background.png').convert()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()
main_game.snake.play_intro_sound()

game_started = False
#snake controls duck and chatgpt help
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE and game_started:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if not game_started:
                game_started = True
            directions = {pygame.K_UP: Vector2(0, -1), pygame.K_RIGHT: Vector2(1, 0), pygame.K_DOWN: Vector2(0, 1), pygame.K_LEFT: Vector2(-1, 0)}
            if event.key in directions and main_game.snake.direction != -directions[event.key]:
                main_game.snake.direction = directions[event.key]

    screen.blit(background_image, (0, 0))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

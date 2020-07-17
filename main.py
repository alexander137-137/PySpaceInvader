import pygame
from characters.enemy import Enemy
from characters.hero import Hero
from typing import List
from pygame import mixer
import copy


class BaseWindow:
    def __init__(self):
        # Init game
        pygame.init()
        self.running = True
        self.stop_running = False
        # Create the screen
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        # Background image
        self.background_image = pygame.image.load("images/background.jpg")


class GameWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        # Title and Icon
        pygame.display.set_caption("Space Invader")

        # Boundary
        self.min_boundary_x = 0
        self.max_boundary_x = self.width - 64
        self.min_boundary_y = 0
        self.max_boundary_y = self.height - 64

        # Music
        mixer.music.load("sound/background.wav")
        mixer.music.play()
        self.bullet_sound = mixer.Sound("sound/laser.wav")
        self.collision_sound = mixer.Sound("sound/explosion.wav")

        # Player
        self.hero = Hero()
        self.hero_image = pygame.image.load(self.hero.get_image())
        self.hero.set_mask(pygame.mask.from_surface(self.hero_image))

        self.bullet = self.hero.get_bullet()
        self.bullet_image = pygame.image.load(self.bullet.get_image())
        self.bullet.set_mask(pygame.mask.from_surface(self.bullet_image))

        self.enemy = Enemy()
        self.enemy_image = pygame.image.load(self.enemy.get_image())
        self.enemy.set_mask(pygame.mask.from_surface(self.enemy_image))
        self.enemies = self.get_enemy(1)

        # Score and level
        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score_text = self.font.render(f"Score: {str(self.score_value)}", True, (0, 255, 0))

        self.level = 1
        self.level_text = self.font.render(f"Level: {self.level}", True, (0, 255, 0))

        # Game over
        self.lose = False
        self.stop_count = 0
        self.game_over_font = pygame.font.Font('freesansbold.ttf', 64)
        self.game_over_text = self.game_over_font.render("GAME OVER", True, (255, 255, 255))

    def start(self):
        # Game Loop
        clock = pygame.time.Clock()

        while self.running:
            # fps = 60
            # clock.tick(fps)
            self.redraw_window()

            if self.lose:
                self.stop_count += 1
                if self.stop_count > 180:
                    self.running = False
                else:
                    continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.hero.move_left()
                if self.hero.get_x_cord() <= self.min_boundary_x:
                    self.hero.set_x_cord(self.min_boundary_x)
            if keys[pygame.K_RIGHT]:
                self.hero.move_right()
                if self.hero.get_x_cord() >= self.max_boundary_x:
                    self.hero.set_x_cord(self.max_boundary_x)
            if keys[pygame.K_UP]:
                self.hero.move_up()
                if self.hero.get_y_cord() <= self.min_boundary_y:
                    self.hero.set_y_cord(self.min_boundary_y)
            if keys[pygame.K_DOWN]:
                self.hero.move_down()
                if self.hero.get_y_cord() >= self.max_boundary_y:
                    self.hero.set_y_cord(self.max_boundary_y)
            if keys[pygame.K_SPACE]:
                if not self.bullet.get_state():
                    self.bullet_sound.play()
                    self.hero.load_bullet()

            if self.bullet.get_state():
                self.hero.fire_bullet(self.enemies, self.update_scoreboard)

            self.start_attack()

    def redraw_window(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.level_text, (10, 10))
        self.screen.blit(self.score_text, (self.width-self.score_text.get_width()-10, 10))

        if self.lose:
            self.screen.blit(self.game_over_text, (self.width/2 - self.game_over_text.get_width()/2, 250))

        if self.bullet.get_state():
            self.screen.blit(self.bullet_image, (self.bullet.get_x_cord(), self.bullet.get_y_cord()))

        self.screen.blit(self.hero_image, (self.hero.get_x_cord(), self.hero.get_y_cord()))

        for enemy in self.enemies:
            self.screen.blit(self.enemy_image, (enemy.get_x_cord(), enemy.get_y_cord()))

        pygame.display.update()

    def start_attack(self):
        for enemy in self.enemies:
            enemy.start_moving()
            if enemy.get_x_cord() >= self.max_boundary_x:
                enemy.move_down()
            if enemy.get_x_cord() <= self.min_boundary_x:
                enemy.move_down()
            if enemy.get_y_cord() >= 400:
                self.game_over()

    def update_scoreboard(self):
        self.score_value += 1
        self.score_text = self.font.render(f"Score: {str(self.score_value)}", True, (0, 255, 0))

    def get_enemy(self, amount):
        index = 0
        enemy_list: List[Enemy] = []

        while index <= amount:
            enemy = copy.copy(self.enemy)
            enemy.set_coord()
            enemy_list.append(enemy)
            index += 1

        return enemy_list

    def game_over(self):
        self.lose = True


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.title = self.font.render("Press the mouse to begin", 1, (255, 255, 255))

    def start(self):
        while self.running:
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title, (self.width/2 - self.title.get_width()/2, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game = GameWindow()
                    game.start()
        pygame.quit()


main_window = MainWindow()
main_window.start()


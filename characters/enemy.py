from characters.character import Character
import random


class Enemy(Character):
    def __init__(self):
        self.image = "images/enemy.png"
        super().__init__(self.image)
        self.character_vel_x = 2
        self.character_vel_y = 40

    def set_coord(self):
        self.x_coord = random.randint(0, 736)
        self.y_coord = random.randint(50, 150)

    def start_moving(self):
        self.x_coord += self.character_vel_x

    def move_down(self):
        self.character_vel_x = abs(self.character_vel_x) if self.x_coord <= 0 else -self.character_vel_x
        self.y_coord += self.character_vel_y

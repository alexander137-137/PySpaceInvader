from characters.character import Character
from characters.ammo.bullet import Bullet


class Hero(Character):
    def __init__(self):
        self.image = "images/hero.png"
        super().__init__(self.image)
        self.x_coord = 370
        self.y_coord = 480
        self.character_vel_x = 10
        self.character_vel_y = 10
        self.bullet = Bullet()

    def set_x_cord(self, x):
        self.x_coord = x

    def set_y_cord(self, y):
        self.y_coord = y

    def get_bullet(self):
        return self.bullet

    def move_right(self):
        self.x_coord += self.character_vel_x

    def move_left(self):
        self.x_coord += -self.character_vel_x

    def move_up(self):
        self.y_coord -= self.character_vel_y

    def move_down(self):
        self.y_coord += self.character_vel_y

    def load_bullet(self):
        self.bullet.set_position(self.x_coord + 10, self.y_coord + 20)

    def fire_bullet(self, enemies, callback):
        self.bullet.move(enemies, callback)



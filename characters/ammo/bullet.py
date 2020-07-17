from characters.character import Character

class Bullet(Character):
    def __init__(self):
        self.image = "images/bullet.png"
        super().__init__(self.image)
        self.character_vel_y = 5
        self.is_ready = False
        self.stop_moving = False

    def get_state(self):
        return self.is_ready

    def set_position(self, x, y):
        self.is_ready = True
        self.x_coord, self.y_coord = x, y

    def move(self, enemies, callback):
        if self.stop_moving:
            self.is_ready = False
            self.stop_moving = False
        else:
            self.y_coord -= self.character_vel_y
            self.stop_moving = True if self.y_coord <= 0 else False
            for enemy in enemies:
                if self.collide(enemy):
                    enemies.remove(enemy)
                    self.stop_moving = True
                    callback()

    def collide(self, obj2):
        offset_x = obj2.x_coord - self.x_coord
        offset_y = obj2.y_coord - self.y_coord
        return self.get_mask().overlap(obj2.get_mask(), (offset_x, offset_y))

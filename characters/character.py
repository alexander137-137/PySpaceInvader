class Character:
    def __init__(self, image):
        self.image = image
        self.x_coord = None
        self.y_coord = None
        self.character_vel_x = None
        self.character_vel_y = None
        self.mask = None

    def get_x_cord(self):
        return self.x_coord

    def get_y_cord(self):
        return self.y_coord

    def get_image(self):
        return self.image

    def get_mask(self):
        return self.mask

    def set_mask(self, mask):
        self.mask = mask

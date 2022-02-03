#the settings of game

class Settings():
    'reserve the settings of the game'

    def __init__(self):
        'initialize the settings of game'
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 0.75

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height   = 15
        self.bullet_color = (60, 60, 60)
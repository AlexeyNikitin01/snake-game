from random import randrange


from pygame import draw, Rect


class Food:
    def __init__(self, setting):
        self.setting = setting
        self.food_location = [randrange(3, 55)*10,
                              randrange(9, 55)*10]

    def draw_food(self, game_screen):
        draw.rect(game_screen, self.setting.color_food, 
                  Rect(self.food_location[0], self.food_location[1],
                       self.setting.h_food, self.setting.w_food))

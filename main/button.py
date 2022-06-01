from pygame import draw, Rect, font


class Button:
    def __init__(self, game_screen, msg, setting):
        self.screen = game_screen
        self.screen_rect = game_screen.get_rect()
        self.msg = msg

        self.color = setting.color_bg_button
        self.h, self.w = setting.h_button, setting.w_button

        self.text_color = setting.text_button_color
        self.size = setting.size_text_button
        self.text_font = font.Font(font.match_font('arial'), self.size)

        self.rect = Rect(0, 0, self.w, self.h)
        self.rect.center = self.screen_rect.center

        self.show_button()

    def show_button(self):
        self.msg_image = self.text_font.render(self.msg, True, 
                                      self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class MenuButton(Button):
    def __init__(self, game_screen, msg, setting):
        super().__init__(game_screen, msg, setting)
        self.rect = self.rect.move(0, -100)
        self.show_button()


class ExitButton(Button):
    def __init__(self, game_screen, msg, setting):
        super().__init__(game_screen, msg, setting)
        self.rect = self.rect.move(0, 100)
        self.show_button()


class PauseButton(Button):
    def __init__(self, game_screen, msg, setting):
        super().__init__(game_screen, msg, setting)

from pygame import draw, Rect, font


class Score:
    def __init__(self, setting, game_screen):
        """Initial score setting"""
        self.color = setting.color_score
        self.game_screen = game_screen
        self.size = 60
        self.font_score = font.Font(font.match_font('arial'), self.size)
        self.score = 0
        self.x, self.y = (100, 2)

    def show_score(self):
        text = str(self.score)
        text_surface = self.font_score.render(text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.game_screen.blit(text_surface, text_rect)


class TheBestScore(Score):
    def __init__(self, setting, game_screen):
        super().__init__(setting, game_screen)
        self.score, self.score_int = self.read_file_the_best_score()
        self.x, self.y = (400, 2)
        
    @staticmethod
    def read_file_the_best_score():
        with open('best_score.txt', 'r') as f:
            score = f.readline()
            score_int = int(score.split()[-1])
        return score, score_int

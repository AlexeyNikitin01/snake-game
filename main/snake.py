from pygame import draw, Rect


class Snake:
    def __init__(self, setting):
        self.color_snake = setting.color_snake
        self.head_snake = setting.head_snake
        self.body_snake = setting.body_snake
        self.direction = 'RIGHT'

    def move_snake(self):
        """Moving snake"""
        if self.direction == 'RIGHT':
            self.head_snake[0] += 10
        elif self.direction == 'LEFT':
            self.head_snake[0] -= 10
        elif self.direction == 'UP':
            self.head_snake[1] -= 10
        elif self.direction == 'DOWN':
            self.head_snake[1] += 10
        self.body_snake.insert(0, list(self.head_snake))
        self.body_snake.pop()

    def draw_snake(self, game_screen):
        """Draw body_snake snake on screen of game"""
        for pos in self.body_snake:
            draw.rect(game_screen, self.color_snake,
                      Rect(pos[0], pos[1], 10, 10))

from sys import exit
from random import randrange


from pygame import init, display, time, image
from pygame import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE, event


from snake import Snake
from food import Food
from setting import Setting
from score import Score, TheBestScore


class SnakeGame:
    def __init__(self):
        init()
        display.set_caption('SnakeGame')

        self.setting_game = Setting()

        self.screen = display.set_mode((self.setting_game.h, self.setting_game.w))
        self.bg_color = self.setting_game.color
        self.bg = image.load('static/bg.png')

        self.score = Score(self.setting_game, self.screen)
        self.bs = TheBestScore(self.setting_game, self.screen)
        self.food = Food(self.setting_game)
        self.snake = Snake(self.setting_game)

    def check_events(self, events):
        """Respond to keypresses events"""
        for event in events:
            time.delay(50)
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and not self.snake.direction == 'LEFT':
                    self.snake.direction = 'RIGHT'
                elif event.key == K_LEFT and not self.snake.direction == 'RIGHT':
                    self.snake.direction = 'LEFT'
                elif event.key == K_UP and not self.snake.direction == 'DOWN':
                    self.snake.direction = 'UP'
                elif event.key == K_DOWN and not self.snake.direction == 'UP':
                    self.snake.direction = 'DOWN'
                elif event.key == K_ESCAPE:
                    exit()

    def food_collision(self):
        if self.food.food_location == self.snake.head_snake:
            self.snake.body_snake.insert(0, list(self.snake.head_snake))
            self.food.food_location = [randrange(3, 550/10)*10,
                                        randrange(9, 550/10)*10]
            self.score.score += 1

    def check_limit(self):
        if (self.snake.head_snake[0] == self.setting_game.w - 10 or \
                self.snake.head_snake[0] == 10) or \
            self.snake.head_snake[1] == self.setting_game.h - 10 or \
                self.snake.head_snake[1] == 70:
            exit()

        for block in self.snake.body_snake[2:]:
            if self.snake.head_snake == block:
                exit()

    def check_best_score(self):
        if self.bs.score_int < self.score.score:
            self.bs.score = 'BEST: ' + str(self.score.score)
            with open('best_score.txt', 'w') as f:
                text = 'BEST: ' + str(self.score.score)
                f.write(text)

    def run_game(self):
        while True:
            time.delay(120)

            self.score.show_score()
            self.bs.show_score()
            self.check_best_score()

            self.food.draw_food(self.screen)
            self.snake.draw_snake(self.screen)
            self.snake.move_snake()

            self.food_collision()
            self.check_limit()
            self.check_events(event.get())

            display.flip()
            self.screen.fill(self.bg_color)
            self.screen.blit(self.bg, (0, 0))


if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()

class Setting:
    def __init__(self):
        self.w = 600
        self.h = 600
        self.color = (230, 230, 230) # Gray

        self.h_food = 10
        self.w_food = 10
        self.color_food = (255, 0, 0) # Red

        self.head_snake = [100, 50]
        self.body_snake = [[100, 50], [90, 50], [80, 50]]
        self.color_snake = (3, 192, 60) # Green

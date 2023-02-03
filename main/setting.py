class Setting:
    def __init__(self):
        self.w = 600
        self.h = 600
        self.color = (230, 230, 230)  # Gray

        self.h_food = 10
        self.w_food = 10
        self.color_food = (255, 0, 0)  # Red

        self.head_snake = [300, 250]
        self.body_snake = [[300, 250], [290, 250], [280, 250]]
        self.color_snake = (3, 192, 60)  # Green

        self.color_score = (0, 0, 0)

        self.color_bg_button = (100, 150, 0)
        self.h_button, self.w_button = (80, 150)
        self.text_button_color = (0, 100, 0)
        self.size_text_button = 60

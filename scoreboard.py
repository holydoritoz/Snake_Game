from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.setpos(0, 270)
        self.clear()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f'Score: {self.score}', False, ALIGNMENT, FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write('GAME OVER', False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

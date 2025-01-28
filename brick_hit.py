import random
import os
import time

class Game:
    def __init__(self):
        self.bricks = ['#' for _ in range(10)]  # 10 bricks
        self.ball_position = 0
        self.score = 0
        self.is_running = True

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Score:", self.score)
        print("Bricks:", " ".join(self.bricks))
        print("Ballp: ", " " * self.ball_position+"O")
        print("Press 'a' to move left, 'd' to move right, or 'h' to hit a brick.")
        
    def move_ball(self, direction):
        if direction == 'a' and self.ball_position > 0:
            self.ball_position -= 1
        elif direction == 'd' and self.ball_position < len(self.bricks) - 1:
            self.ball_position += 1

    def hit_brick(self):
        if self.bricks[self.ball_position] == '#':
            self.bricks[self.ball_position] = ' '
            self.score += 1
            if all(brick == ' ' for brick in self.bricks):
                self.is_running = False

    def play(self):
        while self.is_running:
            self.display()
            move = input("Your move: ").strip().lower()
            if move in ['a', 'd']:
                self.move_ball(move)
            elif move == 'h':
                self.hit_brick()
            else:
                print("Invalid input! Use 'a', 'd', or 'h'.")
            time.sleep(0.2)
        
        print("Game Over! Your final score is:", self.score)

if __name__ == "__main__":
    game = Game()
    game.play()

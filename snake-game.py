import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
SEG_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.direction = "Right"
        self.snake = [(SEG_SIZE*2, SEG_SIZE*2), (SEG_SIZE, SEG_SIZE*2), (0, SEG_SIZE*2)]
        self.food = None
        self.score = 0
        self.game_over = False
        self.root.bind("<Key>", self.change_direction)
        self.create_food()
        self.draw_snake()
        self.move_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="#A020F0", tag="snake")

    def create_food(self):
        while True:
            x = random.randint(0, (WIDTH-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
            y = random.randint(0, (HEIGHT-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
            if (x, y) not in self.snake:
                self.food = (x, y)
                break
        self.canvas.delete("food")
        self.canvas.create_oval(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="yellow", tag="food")

    def move_snake(self):
        if self.game_over:
            return
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= SEG_SIZE
        elif self.direction == "Down":
            y += SEG_SIZE
        elif self.direction == "Left":
            x -= SEG_SIZE
        elif self.direction == "Right":
            x += SEG_SIZE
        new_head = (x, y)
        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in self.snake):
            self.end_game()
            return
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.create_food()
        else:
            self.snake.pop()
        self.draw_snake()
        self.root.after(100, self.move_snake)

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text=f"Game Over!\nScore: {self.score}", fill="white", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

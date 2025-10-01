import tkinter as tk
import random
from tkinter import messagebox

class MemoryMatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Match Game")
        self.pics = [str(i) for i in range(1, 9)] * 2  # 8 คู่
        random.shuffle(self.pics)
        self.buttons = []
        self.flipped = []
        self.matched = set()
        self.create_board()

    def create_board(self):
        for i in range(16):
            btn = tk.Button(self.root, text="", font=("Arial", 20), width=6, height=3,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i//4, column=i%4)
            self.buttons.append(btn)

    def on_click(self, index):
        if index in self.matched or index in self.flipped:
            return
        self.buttons[index].config(text=self.pics[index], state="disabled")
        self.flipped.append(index)
        if len(self.flipped) == 2:
            self.root.after(800, self.check_match)

    def check_match(self):
        i1, i2 = self.flipped
        if self.pics[i1] == self.pics[i2]:
            self.matched.add(i1)
            self.matched.add(i2)
            if len(self.matched) == 16:
                messagebox.showinfo("Congratulations!", "คุณจับคู่ครบทุกคู่แล้ว!")
                self.reset_game()
        else:
            self.buttons[i1].config(text="", state="normal")
            self.buttons[i2].config(text="", state="normal")
        self.flipped = []

    def reset_game(self):
        random.shuffle(self.pics)
        for btn in self.buttons:
            btn.config(text="", state="normal")
        self.flipped = []
        self.matched = set()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryMatch(root)
    root.mainloop()

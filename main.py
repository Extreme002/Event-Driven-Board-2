import tkinter as tk
import random

class GridSquare:
    def __init__(self, root, color, start_row, start_col):
        self.root = root
        self.color = color
        self.current_row = start_row
        self.current_col = start_col
        self.grid_buttons = []
        self.create_grid()

    def create_grid(self):
        for i in range(10):
            row = []
            for j in range(10):
                button = tk.Button(self.root, width=2, height=1, bg='white', command=lambda r=i, c=j: self.toggle_color(r, c))
                button.grid(row=i, column=j)
                row.append(button)
            self.grid_buttons.append(row)

        # Set starting position
        self.grid_buttons[self.current_row][self.current_col]['bg'] = self.color

    def toggle_color(self, row, col):
        current_color = self.grid_buttons[row][col]['bg']
        new_color = 'black' if current_color == 'white' else 'white'
        self.grid_buttons[row][col]['bg'] = new_color

    def move(self):
        options = self.get_available_moves()
        if options:
            new_row, new_col = random.choice(options)
            self.grid_buttons[self.current_row][self.current_col]['bg'] = 'white'
            self.current_row, self.current_col = new_row, new_col
            self.grid_buttons[self.current_row][self.current_col]['bg'] = self.color
        self.root.after(1000, self.move)

    def get_available_moves(self):
        options = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = self.current_row + dr, self.current_col + dc
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if self.grid_buttons[new_row][new_col]['bg'] == 'white':
                    options.append((new_row, new_col))
        return options

class BlueSquare(GridSquare):
    def __init__(self, root):
        super().__init__(root, 'light blue', 0, 0)

    def move(self):
        self.highlight_available_moves()
        self.root.after(1000, self.move)

    def highlight_available_moves(self):
        for i in range(10):
            for j in range(10):
                if self.grid_buttons[i][j]['bg'] == 'light blue':
                    self.grid_buttons[i][j]['bg'] = 'white'

        for square in [green_square, orange_square]:
            options = square.get_available_moves()
            for row, col in options:
                self.grid_buttons[row][col]['bg'] = 'light blue'

root = tk.Tk()
green_square = GridSquare(root, 'green', 5, 5)
orange_square = GridSquare(root, 'orange', 2, 2)
blue_square = BlueSquare(root)
root.after(1000, green_square.move)
root.after(1500, orange_square.move)
root.after(2000, blue_square.move)
root.mainloop()

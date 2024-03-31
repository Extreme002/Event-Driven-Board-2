import tkinter as tk
import random
import time

class GridAI:
    def __init__(self, root):
        self.root = root
        self.root.title("Grid Layout")
        self.grid_buttons = []
        self.current_row_green = 5
        self.current_col_green = 5
        self.current_row_orange = 2
        self.current_col_orange = 2

        self.create_grid()
        self.root.after(1000, self.move_green)
        self.root.after(1500, self.move_orange)

    def create_grid(self):
        for i in range(10):
            row = []
            for j in range(10):
                button = tk.Button(self.root, width=2, height=1, bg='white', command=lambda r=i, c=j: self.toggle_color(r, c))
                button.grid(row=i, column=j)
                row.append(button)
            self.grid_buttons.append(row)

        # Set starting positions
        self.grid_buttons[self.current_row_green][self.current_col_green]['bg'] = 'green'
        self.grid_buttons[self.current_row_orange][self.current_col_orange]['bg'] = 'orange'

    def toggle_color(self, row, col):
        current_color = self.grid_buttons[row][col]['bg']
        new_color = 'black' if current_color == 'white' else 'white'
        self.grid_buttons[row][col]['bg'] = new_color

    def move_green(self):
        self.highlight_adjacent_squares(self.current_row_green, self.current_col_green)
        self.root.after(1000, self.select_move_green)

    def move_orange(self):
        self.highlight_adjacent_squares(self.current_row_orange, self.current_col_orange)
        self.root.after(1000, self.select_move_orange)

    def highlight_adjacent_squares(self, row, col):
        # Highlight adjacent squares in light blue
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if self.grid_buttons[new_row][new_col]['bg'] == 'white':
                    self.grid_buttons[new_row][new_col]['bg'] = 'light blue'

    def select_move_green(self):
        options = self.get_available_moves(self.current_row_green, self.current_col_green)
        if options:
            new_row, new_col = random.choice(options)
            self.grid_buttons[self.current_row_green][self.current_col_green]['bg'] = 'white'
            self.current_row_green, self.current_col_green = new_row, new_col
            self.grid_buttons[self.current_row_green][self.current_col_green]['bg'] = 'green'
        self.root.after(1000, self.deselect_squares)

    def select_move_orange(self):
        options = self.get_available_moves(self.current_row_orange, self.current_col_orange)
        if options:
            new_row, new_col = random.choice(options)
            self.grid_buttons[self.current_row_orange][self.current_col_orange]['bg'] = 'white'
            self.current_row_orange, self.current_col_orange = new_row, new_col
            self.grid_buttons[self.current_row_orange][self.current_col_orange]['bg'] = 'orange'
        self.root.after(1000, self.deselect_squares)

    def get_available_moves(self, row, col):
        options = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if self.grid_buttons[new_row][new_col]['bg'] == 'light blue':
                    options.append((new_row, new_col))
        return options

    def deselect_squares(self):
        for i in range(10):
            for j in range(10):
                if self.grid_buttons[i][j]['bg'] == 'light blue':
                    self.grid_buttons[i][j]['bg'] = 'white'
        self.root.after(1000, self.move_green)
        self.root.after(1000, self.move_orange)

root = tk.Tk()
ai = GridAI(root)
root.mainloop()

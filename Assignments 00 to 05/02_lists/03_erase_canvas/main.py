import tkinter as tk

class EraserCanvas(tk.Canvas):
    def __init__(self, master, width, height, cell_size):
        super().__init__(master, width=width, height=height, bg='white')
        self.cell_size = cell_size  
        self.grid = []  
        self.create_grid()
        self.eraser = None  
        self.bind("<B1-Motion>", self.on_drag)

    def create_grid(self):
        """ Create a grid of blue cells on the canvas. """
        # Calculate how many rows and columns fit on the canvas
        rows = int(self.winfo_reqheight() / self.cell_size)
        cols = int(self.winfo_reqwidth() / self.cell_size)

        # Loop through rows and columns to create cells
        for row in range(rows):
            row_cells = [] 
            for col in range(cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                # Create a rectangle (cell) and add it to the grid
                cell = self.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
                row_cells.append(cell)
            self.grid.append(row_cells)

    def on_drag(self, event):
        """ Erase (change color to white) cells in contact with the eraser. """
        # Calculate the grid cell position based on mouse coordinates
        cell_x = event.x // self.cell_size
        cell_y = event.y // self.cell_size

        # Loop through nearby cells (3x3 grid around the mouse location)
        for dx in range(-1, 2): 
            for dy in range(-1, 2):
                x = cell_x + dx
                y = cell_y + dy
                
                if 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid):
                    self.itemconfig(self.grid[y][x], fill='white')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Canvas Eraser")
    canvas = EraserCanvas(root, 400, 400, 20)
    canvas.pack()  
    root.mainloop()

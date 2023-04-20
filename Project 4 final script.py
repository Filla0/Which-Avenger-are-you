
import tkinter as tk
import random as rd

class PathFinder:
                    
    def __init__(self, root):
        self.root = root
        self.root.title('PathFinder')
        
        self.container1 = tk.Frame(root)
        self.container1.pack(side="left", fill="both", expand=True)
        
        self.grid_values = []
        self.best_path = [] # initialize best_path as an empty list
        self.grid_size = 5 # set grid size to 5 by default
        self.high_score = 0 # initialize high score to 0
        
        # create 'Find best path' button
        self.path_button = tk.Button(self.container1, text="Find best path", background="white")
        self.path_button.pack(side="left")
        self.path_button.bind("<Button-1>", self.find_best_path)
            
        # create label for text
        self.feedback = tk.Label(self.container1, text="", background="white")
        self.feedback.pack(side="left")        

        # create 'Exit program' button
        self.exit_button = tk.Button(self.container1, text="Exit program", background="white")
        self.exit_button.pack(side="left")
        self.exit_button.bind("<Button-1>", self.exit_program)
        
        # create label for high score
        self.high_score_label = tk.Label(self.container1, text="High score: " + str(self.high_score), background="white")
        self.high_score_label.pack(side="left")

        # create 'Create new random field' button
        self.fieldGen_button = tk.Button(self.container1, text="Create new random field", background="white")
        self.fieldGen_button.pack(side="left")
        self.fieldGen_button.bind("<Button-1>", self.generate_field)

        # create canvas for grid display
        self.canvas = tk.Canvas(root, width=250, height=250, background='white')
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.generate_field()
        self.draw_field()
        
    # Create a function to draw a new field     
    def draw_field(self):
        # clear the canvas
        self.canvas.delete("all")        
        # draw the grid values
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid_values[i][j]
                x0, y0 = j * 50, i * 50
                x1, y1 = x0 + 50, y0 + 50
                x2, y2 = x1 + 50, y1 + 50
                color = 'white'
                if (i, j) in self.best_path:
                    color = 'green'
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='black')
                self.canvas.create_text(x0 + 25, y0 + 25, text=str(value), font=('Arial', 20, 'bold'))
                # Add 's' to the bottom left cell
                if i == self.grid_size - 1 and j == 0:
                    self.canvas.create_text(x0 + 10, y1 - 10, text="s", font=('Arial', 10, 'bold'))
                # Add 'f' to the top right cell
                if i == 0 and j == self.grid_size - 1:
                    self.canvas.create_text(x1 - 10, y0 + 10, text="f", font=('Arial', 10, 'bold'))

    # Create a function to generate a new field with random values
    def generate_field(self, event=None):
        self.grid_values = [[rd.randint(0, 99) for j in range(self.grid_size)] for i in range(self.grid_size)]
        self.best_path = []
        self.feedback.configure(text="")
        self.draw_field()

    # Create a function to find the best path
    def find_best_path(self, event=None):
        # set feedback text
        self.feedback.configure(text="Finding best path...")

        # initialize variables
        start = (self.grid_size - 1, 0)
        end = (0, self.grid_size - 1)
        unvisited = {(i, j) for i in range(self.grid_size) for j in range(self.grid_size)}
        distance = {(i, j): -float('inf') for i in range(self.grid_size) for j in range(self.grid_size)}
        distance[start] = self.grid_values[start[0]][start[1]]
        prev = {(i, j): None for i, j in unvisited}

        # loop until all vertices are visited
        while unvisited:
            # get the unvisited vertex with the largest distance
            curr = max(unvisited, key=lambda x: distance[x])
            unvisited.remove(curr)

            # check if current vertex is the end
            if curr == end:
                # traverse the prev dictionary to get the best path
                path = []
                while prev[curr] is not None:
                    path.append(curr)
                    curr = prev[curr]
                path.append(curr)
                path.reverse()

                # update high score if necessary
                total_sum = distance[end]
                if total_sum > self.high_score:
                    self.high_score = total_sum
                    self.high_score_label.configure(text="High score: " + str(self.high_score))

                # set feedback text
                self.feedback.configure(text="Best path found! Total sum: " + str(total_sum))
                # redraw the field
                self.best_path = path
                self.draw_field()
                return

            # update distances and prev values of neighbors of current vertex (only right and up)
            for neighbor in [(curr[0], curr[1] + 1), (curr[0] - 1, curr[1])]:
                if neighbor in unvisited:
                    new_distance = distance[curr] + self.grid_values[neighbor[0]][neighbor[1]]
                    if new_distance > distance[neighbor]:
                        distance[neighbor] = new_distance
                        prev[neighbor] = curr

        # set feedback text if no path was found
        self.feedback.configure(text="No path found.")

# Create a function to exit the program
    def exit_program(self, event=None):
            self.root.destroy()
def main():
    # create the tkinter window
        root = tk.Tk()
    # create the PathFinder instance
        path_finder = PathFinder(root)
    # run the tkinter event loop
        root.mainloop()

    # Create a function to exit the program

if __name__ == "__main__": 
    main()
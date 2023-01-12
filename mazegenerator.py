import random
import matplotlib.pyplot as plt

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[1 for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]
        self.stack = []
        self.current_cell = (0, 0)
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def generate(self):
        self.visited[self.current_cell[0]][self.current_cell[1]] = True
        self.stack.append(self.current_cell)
        while self.stack:
            neighbors = []
            for direction in self.directions:
                x, y = self.current_cell[0] + direction[0], self.current_cell[1] + direction[1]
                if 0 <= x < self.height and 0 <= y < self.width and not self.visited[x][y]:
                    neighbors.append((x, y))
            if neighbors:
                next_cell = random.choice(neighbors)
                self.visited[next_cell[0]][next_cell[1]] = True
                self.stack.append(next_cell)
                x1, y1 = self.current_cell
                x2, y2 = next_cell
                self.grid[(x1 + x2) // 2][(y1 + y2) // 2] = 0
                self.current_cell = next_cell
            else:
                self.current_cell = self.stack.pop()

    def show(self):
        plt.imshow(self.grid, cmap='gray')
        plt.show()

# Example usage:
maze = Maze(20, 20)
maze.generate()
maze.show()

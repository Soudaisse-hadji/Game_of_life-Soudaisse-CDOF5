import copy
import time
import os

def print_grid(grid, iteration):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Iteration: {iteration}")
    for row in grid:
        print(' '.join(['#' if cell else '.' for cell in row]))
    time.sleep(0.5)

def get_neighbors(x, y, grid):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                neighbors += grid[nx][ny]
    return neighbors

def update_grid(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbors = get_neighbors(i, j, grid)
            if grid[i][j]:  # Cell is alive
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0  # Cell dies
            else:  # Cell is dead
                if neighbors == 3:
                    new_grid[i][j] = 1  # Cell becomes alive
    return new_grid

def get_initial_configuration(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    print("Enter initial live cells in format 'row col', one per line. Enter 'done' when finished:")
    while True:
        entry = input()
        if entry.lower() == 'done':
            break
        x, y = map(int, entry.split())
        if 0 <= x < rows and 0 <= y < cols:
            grid[x][y] = 1
        else:
            print("Invalid coordinates. Please enter again.")
    return grid

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = get_initial_configuration(rows, cols)
    iteration = 0

    try:
        while True:
            print_grid(grid, iteration)
            grid = update_grid(grid)
            iteration += 1
    except KeyboardInterrupt:
        print("Game of Life terminated.")

if __name__ == "__main__":
    main()
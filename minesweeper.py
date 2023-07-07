
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
def minesweeper(grid):
    # Define the eight possible directions around a cell
    directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not i == j == 0]

    # Create a new grid to store the results
    result_grid = [[0]*len(row) for row in grid]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # If the cell is a mine, mark it on the result grid and continue
            if grid[row][col] == '#':
                result_grid[row][col] = '#'
                continue

            # Count the number of mines around the cell
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the new cell is within the grid
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]) and grid[new_row][new_col] == '#':
                    result_grid[row][col] += 1

            # Convert the count to a string, as per the specification
            result_grid[row][col] = str(result_grid[row][col])

    return result_grid

# Test the function

grid = [ ["-", "-", "-", "#", "#"],
         ["-", "#", "-", "-", "-"],
         ["-", "-", "#", "-", "-"],
         ["-", "#", "#", "-", "-"],
         ["-", "-", "-", "-", "-"] ]

print(minesweeper(grid))

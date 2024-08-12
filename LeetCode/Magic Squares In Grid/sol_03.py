# Function to check if a 3x3 subgrid starting at (x, y) is a magic square
def check(grid: List[List[int]], x: int, y: int):
    # Extract the 3x3 subgrid from the main grid
    square = [
        [grid[x+0][y+0], grid[x+0][y+1], grid[x+0][y+2]],
        [grid[x+1][y+0], grid[x+1][y+1], grid[x+1][y+2]],
        [grid[x+2][y+0], grid[x+2][y+1], grid[x+2][y+2]],
    ]
    
    # Check if the subgrid satisfies all the conditions of a magic square
    return (
        True
        # Check if all rows sum to 15
        and (square[0][0] + square[0][1] + square[0][2] == 15)
        and (square[1][0] + square[1][1] + square[1][2] == 15)
        and (square[2][0] + square[2][1] + square[2][2] == 15)
        # Check if all columns sum to 15
        and (square[0][0] + square[1][0] + square[2][0] == 15)
        and (square[0][1] + square[1][1] + square[2][1] == 15)
        and (square[0][2] + square[1][2] + square[2][2] == 15)
        # Check if both diagonals sum to 15
        and (square[0][0] + square[1][1] + square[2][2] == 15)
        and (square[0][2] + square[1][1] + square[2][0] == 15)
        # Check if the subgrid contains all distinct numbers from 1 to 9
        and sorted([e for es in square for e in es]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    )

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0  # Initialize the count of magic squares found
        rows = len(grid)  # Get the number of rows in the grid
        
        # Loop over the grid to find potential 3x3 subgrids
        for x in range(0, rows):
            if rows - x < 3:  # If there aren't enough rows left for a 3x3 grid, break the loop
                break
            
            row = grid[x]  # Get the current row
            cols = len(row)  # Get the number of columns in the current row
            
            # Loop through columns to find the starting position of the 3x3 subgrid
            for y in range(0, cols):
                if cols - y < 3:  # If there aren't enough columns left for a 3x3 grid, break the loop
                    break
                
                # Check if the 3x3 subgrid starting at (x, y) is a magic square
                if check(grid, x, y):
                    count += 1  # If it is, increment the count
        
        return count  # Return the total count of magic squares found

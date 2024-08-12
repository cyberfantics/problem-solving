class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        row, col = len(grid), len(grid[0])
        
        # If the grid is smaller than 3x3, return 0 as no magic square can exist
        if row < 3 or col < 3:
            return 0
        
        # Helper function to check if a 3x3 subgrid with center at (i, j) is a magic square
        def isMagicSquare(i, j):
            # Extract the 3x3 subgrid centered at (i, j)
            arr = [
                grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                grid[i][j-1],   grid[i][j],   grid[i][j+1],
                grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
            ]
            
            # Check the sums of rows, columns, and diagonals
            if (
                sum(arr[0:3]) == sum(arr[3:6]) == sum(arr[6:9]) and  # Check all rows
                sum(arr[0:9:3]) == sum(arr[1:9:3]) == sum(arr[2:9:3]) and  # Check all columns
                grid[i-1][j-1] + grid[i+1][j+1] == grid[i+1][j-1] + grid[i-1][j+1] and  # Check diagonals
                max(arr) < 10 and min(arr) > 0 and  # Ensure all numbers are between 1 and 9
                len(arr) == len(set(arr))  # Ensure all numbers are distinct
            ):
                return True
        
        # Initialize the count of magic squares found
        count = 0
        
        # Traverse the grid, considering the center of potential 3x3 subgrids
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                # Check if the current cell (i, j) has a value of 5 (necessary for a magic square)
                # and if the subgrid centered at (i, j) is a magic square
                if grid[i][j] == 5 and isMagicSquare(i, j):
                    count += 1
        
        # Return the total count of magic squares found
        return count

class Solution:
    def numMagicSquaresInside(self, grid):
        def isMagicSquare(grid, startRow, startCol):
            nums = []
            for i in range(3):
                for j in range(3):
                    nums.append(grid[startRow + i][startCol + j])
            
            nums.sort()
            if nums != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            
            magicSum = 15
            
            # Check all rows
            for i in range(3):
                if grid[startRow + i][startCol] + grid[startRow + i][startCol + 1] + grid[startRow + i][startCol + 2] != magicSum:
                    return False
            
            # Check all columns
            for j in range(3):
                if grid[startRow][startCol + j] + grid[startRow + 1][startCol + j] + grid[startRow + 2][startCol + j] != magicSum:
                    return False
            
            # Check diagonals
            if grid[startRow][startCol] + grid[startRow + 1][startCol + 1] + grid[startRow + 2][startCol + 2] != magicSum:
                return False
            
            if grid[startRow + 2][startCol] + grid[startRow + 1][startCol + 1] + grid[startRow][startCol + 2] != magicSum:
                return False
            
            return True
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagicSquare(grid, i, j):
                    count += 1
        
        return count

# Example usage:
s = Solution()
grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
print(s.numMagicSquaresInside(grid))  # Output: 1

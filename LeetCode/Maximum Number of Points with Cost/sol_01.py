class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        # Previous row's max points
        prev_row = points[0]
        
        # Iterate over each row starting from the second one
        for i in range(1, m):
            # Initialize the current row
            current_row = [0] * n
            
            # Left-to-right pass
            left_max = [0] * n
            left_max[0] = prev_row[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j-1] - 1, prev_row[j])
            
            # Right-to-left pass
            right_max = [0] * n
            right_max[-1] = prev_row[-1]
            for j in range(n-2, -1, -1):
                right_max[j] = max(right_max[j+1] - 1, prev_row[j])
            
            # Update current row's max points considering left and right maximums
            for j in range(n):
                current_row[j] = points[i][j] + max(left_max[j], right_max[j])
            
            # Update previous row to current row
            prev_row = current_row
        
        # The answer is the maximum value in the last processed row
        return max(prev_row)

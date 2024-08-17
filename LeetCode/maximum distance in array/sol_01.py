class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize variables
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        # Iterate through the arrays starting from the second array
        for i in range(1, len(arrays)):
            # Calculate distances using current array's first and last elements
            max_distance = max(max_distance, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            
            # Update min_val and max_val with the current array's elements
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_distance

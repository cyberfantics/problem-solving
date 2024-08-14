class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Sort the array to make it easier to count pairs with a specific distance
        nums.sort()
        
        # Define the binary search range: 
        # smallest distance (`left`) and largest distance (`right`)
        left, right = 0, nums[-1] - nums[0]
        
        # Helper function to count how many pairs have a distance less than or equal to 'mid'
        def count_pairs_with_distance_less_than_or_equal_to(mid):
            count, left = 0, 0
            # Use a sliding window to count pairs
            for right in range(len(nums)):
                # Move the left pointer until the difference is <= mid
                while nums[right] - nums[left] > mid:
                    left += 1
                # Add the number of valid pairs with the current 'right' element
                count += right - left
            return count
        
        # Binary search for the smallest distance that has exactly 'k' pairs less than or equal to it
        while left < right:
            mid = (left + right) // 2
            if count_pairs_with_distance_less_than_or_equal_to(mid) >= k:
                # If we found at least 'k' pairs, try a smaller distance
                right = mid
            else:
                # Otherwise, look for a larger distance
                left = mid + 1
        
        # 'left' will be the k-th smallest distance at the end of the binary search
        return left

class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()

        n = len(nums)

        def func(x):
            count, left, right = 0, 0, 0 

            for right in range(n):
                while nums[right] - nums[left] > x:
                    left += 1 
                count += right-left 

            return count 

        low, high = 0, nums[-1]-nums[0]

        while low <= high:
            mid = (low+high)//2 

            if func(mid) < k:
                low = mid + 1 
            else:
                high = mid - 1 

        return low 
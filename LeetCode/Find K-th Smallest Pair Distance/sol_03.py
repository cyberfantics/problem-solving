class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = math.inf
        for i in range(len(nums)-1):
            m = min((nums[i+1]-nums[i],m))
            if m == 0:
                break
        def binary_min(elem):
            # Find the smallest index such that arr[i] >= elem
            left = 0
            right = len(nums)-1
            while left < right:
                mid = left + (right-left)//2
                if nums[mid] < elem:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binary_max(elem):
            # Find the smallest index such that arr[i] < elem
            left = 0
            right = len(nums)
            while left < right:
                mid = left + (right-left)//2
                if nums[mid] >= elem:
                    left = mid + 1
                else:
                    right = mid
            return left
        def condition(distance):
            count, i, j = 0, 0, 0
            while i < len(nums) or j < len(nums):
                while j < len(nums) and nums[j] - nums[i] <= distance:  # move fast pointer
                    j += 1
                count += j - i - 1  # count pairs
                i += 1  # move slow pointer
            return count >= k
        left, right = m, nums[-1]-nums[0]
        #We consider all the ranges possible from the smallest to the biggest
        # ->
        print('boundaries:',left,right)
        while left < right:
            mid = left + (right-left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
class Solution:
    def maxDistance(self, arrays):
        res, curMin, curMax = 0, float('inf'), float('-inf')

        for a in arrays:
            res = max((curMax - a[0]), (a[-1] - curMin), res)
            curMax, curMin = max(curMax, a[-1]), min(curMin, a[0])
        return res
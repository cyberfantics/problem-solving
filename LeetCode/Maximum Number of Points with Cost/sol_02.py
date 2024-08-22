class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [0] * n
        for i in range(m):
            newDp = [0] * n
            for j in range(n):
                point = points[i][j]
                if i > 0:
                    point += dp[j]
                if j > 0:
                    if point > newDp[j - 1] - 1:
                        k = j
                        while k >= 0 and newDp[k] < point:
                            newDp[k] = point
                            k -= 1
                            point -= 1
                    else:
                        newDp[j] = newDp[j - 1] - 1
                else:
                    newDp[j] = point
            dp = newDp
        return max(dp)
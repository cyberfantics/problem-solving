class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        prevNum = [arrays[0][0], arrays[0][-1]]
        result = float('-inf')
        for i in range(1, len(arrays)):
            result = max(result, abs(arrays[i][-1] - prevNum[0]), abs(prevNum[1] - arrays[i][0]))
            prevNum[0] = min(prevNum[0], arrays[i][0])
            prevNum[1] = max(prevNum[1], arrays[i][-1])
        
        return result
            

        
            
        
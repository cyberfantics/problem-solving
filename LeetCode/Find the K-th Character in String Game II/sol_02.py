class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        p = int(log(k)/log(2)+1) #Min number of operations p needed
        count = 0
        while(p>0):
            l_prev = pow(2,p-1) #length of prev
            if(k>l_prev): #if on the second half, add operation
                count+=operations[p-1]
                k = k-l_prev
            p-=1
        return chr(ord('a')+count%26)
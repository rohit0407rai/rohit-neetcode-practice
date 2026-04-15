class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        cnt=0
        for i in nums:  
            if i == 1:
                cnt+=1
            res = max(res, cnt)
            if i==0:
                cnt=0
        
            
        return max(res, cnt)
                
        
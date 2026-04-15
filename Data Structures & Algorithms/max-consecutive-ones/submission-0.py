class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        globalcount = 0
        count = 0;
        for num in nums:
            
            if num ==1 :
                count+=1
        
            if count > globalcount:
                globalcount = count

            if num ==0 :
                count =0
                
        return globalcount
        
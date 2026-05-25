class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j] != 1:
                    break
                cnt +=1
            res= max(res, cnt)
            cnt=0
        return res
                
        
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        removeIndex = []
        for i in range(len(nums)):
            if nums[i] == val:
                removeIndex.append(nums[i])
        for i in removeIndex:
            nums.remove(i)
           
            
        return len(nums)
        
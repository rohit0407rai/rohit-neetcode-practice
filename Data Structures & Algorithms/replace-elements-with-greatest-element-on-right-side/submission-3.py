class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax=-1
        ans = [0] * len(arr)
        n =len(arr)
        for i in range(n-1, -1, -1): 
            #-1 not gets included
            ans[i]= rightMax
            rightMax = max(rightMax, arr[i])
        return ans

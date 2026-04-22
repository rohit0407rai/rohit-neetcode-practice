class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax=0
        ans = [0] * len(arr)
        i = len(arr)-1
        if len(arr) == 1:
            return [-1]
        while i>0:
            if i == len(arr)-1:
                rightMax=-1
                ans[i]=rightMax
            rightMax= max(rightMax, arr[i])
            ans[i-1]=rightMax
            i-=1
        return ans
                

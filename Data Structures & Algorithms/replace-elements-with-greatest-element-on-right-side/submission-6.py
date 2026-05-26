class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=-1
        for i in range(len(arr)):
            res=-1
            if i==len(arr)-1:
                arr[i]=-1
                break
            for j in range(i+1, len(arr)):
                res = max(res,arr[j])
            arr[i]=res
        return arr

        
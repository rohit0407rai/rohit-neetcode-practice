class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        for i in range(len(arr)):
            maxVal=-1
            if(i== len(arr)-1):
                arr[i]=maxVal
                break
            for j in range(i+1, len(arr)):
                maxVal = max(maxVal, arr[j])
            arr[i]=maxVal
        return arr


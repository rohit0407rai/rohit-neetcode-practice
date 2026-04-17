class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
           
            maxIndex= i+1
            if( i == len(arr)-1):
                arr[i]=-1
                break
            
            for j in range(i+1, len(arr)):
                if arr[maxIndex]<arr[j]:
                    maxIndex=j
                
                

            arr[i]=arr[maxIndex]
                

        return arr
                

                
        
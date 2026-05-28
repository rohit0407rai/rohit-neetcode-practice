class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum=0
        stck=[]
        for i in range(len(operations)):
            if operations[i] == "+":
                
                sum = sum+stck[-1]+stck[-2]
                stck.append(stck[-1]+stck[-2])
            elif operations[i] == "D":
                
                sum = sum+stck[-1]*2
                stck.append(stck[-1]*2)
            elif operations[i] == "C":
                sum = sum - stck[-1]
                stck.pop()
            else:
                stck.append(int(operations[i]))
                sum =sum+ int(operations[i])
        return sum

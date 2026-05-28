class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck=[]
        for i in range(len(operations)):
            if operations[i] not in ["+", "D", "C"]:
                stck.append(int(operations[i]))
            if operations[i] == "+":
                stck.append(int(stck[-1])+int(stck[-2]))
            if operations[i] =="D":
                stck.append(stck[-1]*2)
            if operations[i]=="C":
                stck.pop()
        return sum(stck)

        
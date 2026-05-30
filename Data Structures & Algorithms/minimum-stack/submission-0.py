class MinStack:
  

    def __init__(self):
        self.stack =[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minVal = 2**31 - 1
        for i in self.stack:
            minVal =min(minVal, i)
        return minVal

        

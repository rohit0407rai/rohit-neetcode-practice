class MinStack:
  

    def __init__(self):
        self.stack =[]
        self.minVal = float("inf")
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minVal= val
        else:
            diff = val - self.minVal
            self.stack.append(diff)
            self.minVal = min(self.minVal, val)
        


    def pop(self) -> None:
        if not self.stack:
            return
        pop= self.stack.pop()
        if pop<0:
            self.minVal= self.minVal-pop
        

    def top(self) -> int:
        if not self.stack:
            return
        if self.stack[-1]>0:
            return self.stack[-1]+self.minVal
        else:
            return self.minVal
        

    def getMin(self) -> int:
        return self.minVal

        

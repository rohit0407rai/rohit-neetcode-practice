class BrowserHistory:

    def __init__(self, homepage: str):
        self.backHistory =[]
        self.backHistory.append(homepage)
        self.frontHistory=[]

        
        

    def visit(self, url: str) -> None:
        self.backHistory.append(url)
        if self.frontHistory:
            while self.frontHistory:
                self.frontHistory.pop()


        

    def back(self, steps: int) -> str:
        while self.backHistory and steps!=0 and len(self.backHistory)!=1:
            pop = self.backHistory.pop()
            self.frontHistory.append(pop)
            steps -=1
        return self.backHistory[-1]


        

            
        

    def forward(self, steps: int) -> str:
        while self.frontHistory and steps!=0:
            pop = self.frontHistory.pop()
            self.backHistory.append(pop)
            steps-=1
        return self.backHistory[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
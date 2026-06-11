class BrowserHistory:

    def __init__(self, homepage: str):
        self.browserHistory =[]
        self.browserHistory.append(homepage)
        self.curr = 0
        
        

    def visit(self, url: str) -> None:
        if self.browserHistory and self.curr!= len(self.browserHistory)-1:
            self.browserHistory = self.browserHistory[:self.curr+1]
            self.browserHistory.append(url)
            self.curr += 1
        else:
            self.browserHistory.append(url)
            self.curr += 1

        

    def back(self, steps: int) -> str:
        while self.browserHistory and len(self.browserHistory) != 1 and steps != 0 and self.curr !=0:
            self.curr -=1
            steps -=1 
        return self.browserHistory[self.curr]


        

            
        

    def forward(self, steps: int) -> str:
        while self.browserHistory and steps!=0 and self.curr != len(self.browserHistory)-1:
            self.curr += 1
            steps-=1
        return self.browserHistory[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
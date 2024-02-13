class node:
    def __init__(self, site, next= None,prev= None):
        self.site = site
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = node(homepage)
        self.last = self.homepage
        

    def visit(self, url: str) -> None:
        visited = node(url)
        self.last.next = visited
        visited.prev = self.last
        self.last = visited

    def back(self, steps: int) -> str:
        while steps>0 and self.last.prev:
            self.last = self.last.prev
            steps-=1
       
        return self.last.site



    def forward(self, steps: int) -> str:
        while steps>0 and self.last.next:
            self.last = self.last.next
            steps-=1
        if self.last == None:
            return self.last
        return self.last.site



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
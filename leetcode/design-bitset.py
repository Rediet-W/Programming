class Bitset:

    def __init__(self, size: int):
        self.bs = [False for i in range(size)]
        self.bsflipped = [True for i in range(size)]
        self.size = size
        self.ones = 0
        

    def fix(self, idx: int) -> None:
        if not self.bs[idx]:
            self.ones +=1
        self.bs[idx] = True
        self.bsflipped[idx] = False

    def unfix(self, idx: int) -> None:
        if self.bs[idx]:
            self.ones -=1
        self.bs[idx] = False
        self.bsflipped[idx] = True
           

    def flip(self) -> None:
        self.ones = self.size - self.ones
        self.bs, self.bsflipped = self.bsflipped, self.bs


    def all(self) -> bool:
        return self.ones == self.size
                 

    def one(self) -> bool:
        return self.ones > 0 
        

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        ans = ""
        for i in self.bs:
            if i:
                ans += "1"
            else:
                ans += '0'
        return ans

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
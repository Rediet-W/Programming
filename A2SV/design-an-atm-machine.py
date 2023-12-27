class ATM:

    def __init__(self):
        self.d = [20,50, 100, 200, 500]
        self.count = [0]* 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.count[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        tot = 0
        for i in range(len(self.d)-1,-1,-1):
            used = min(amount // self.d[i], self.count[i])
            ans[i] = used
            tot += used * self.d[i]
            amount -= used * self.d[i]

        if amount != 0:
            return [-1]
        for i in range(len(self.d)):
            self.count[i] -= ans[i]
        return ans
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
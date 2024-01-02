class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl= timeToLive
        self.token = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token and currentTime < self.token[tokenId]:
            self.token[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        c = 0
        for i,n in self.token.items():
            if currentTime < n:
                c +=1
        return c
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
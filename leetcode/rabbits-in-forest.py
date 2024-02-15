class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = 0
        dictt= defaultdict(int)
        for i in answers:
            if i == 0:
                rabbits += 1
            else:
                dictt[i] += 1
                if dictt[i] == 1:
                    rabbits += i+1
                elif dictt[i] % (i+1) == 0:
                    dictt[i] = 0

        return rabbits
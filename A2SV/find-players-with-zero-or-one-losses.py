class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        have_not_lost = []
        one_loss= []
        dictionary = {}
        for winner,loser in matches:
            dictionary[winner] = dictionary.get(winner,0)
            dictionary[loser] = dictionary.get(loser,0) + 1
        
        for player,losses in dictionary.items():
            if losses == 1:
                one_loss.append(player)
            if losses == 0:
                have_not_lost.append(player)
        answer = [sorted(have_not_lost),sorted(one_loss)]
        return answer

            


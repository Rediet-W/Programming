class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score(left, right, turn, player1, player2):

            if left > right:
                return True if player1>= player2 else False

            l = score(left + 1, 
            right,
            2 if turn== 1 else 1, 
            player1 + nums[left] if turn==1 else player1, 
            player2 + nums[left] if turn == 2 else player2)

            r = score(left, 
            right - 1,
            2 if turn== 1 else 1, 
            player1 + nums[right] if turn==1 else player1, 
            player2 + nums[right] if turn == 2 else player2)

            if turn == 1:
                return l or r
            return l and r

        return score(0, len(nums)-1, 1,0,0)
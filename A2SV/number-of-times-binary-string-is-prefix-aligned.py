class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        one = 0
        count = 0
        mx = 0
        for i in flips:
            one +=1
            mx = max(mx,i)
            if one == mx:
                count+=1
        return count

        
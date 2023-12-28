class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total = sum(nums)

        best = total
        score = total
        answer = [0]

        for i in range(len(nums)):
            if nums[i] == 0:
                score+=1
            else:
                score-=1

            if best==score:
                answer.append(i+1)
            elif best < score:
                best = score
                answer = [i +1]
        return answer
        

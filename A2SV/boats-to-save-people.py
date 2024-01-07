class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        left, right = 0, len(people) - 1
        people.sort(reverse=True)
        while left<= right:
           remain = limit - people[left]
           boat +=1
           left+=1
           if left <= right and remain>= people[right]:
               right -=1
        return boat
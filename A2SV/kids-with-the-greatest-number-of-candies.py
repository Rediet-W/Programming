class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_no_of_candies=[]
        maximum = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                greatest_no_of_candies.append(True)
            else:
                greatest_no_of_candies.append(False)
        return greatest_no_of_candies

        
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_pointer = 0
        second_pointer = 0
        Intersection = []

        while first_pointer < len(firstList) and second_pointer < len(secondList):
            firststart = firstList[first_pointer][0]
            firstend = firstList[first_pointer][1]
            secondstart = secondList[second_pointer][0]
            secondend = secondList[second_pointer][1]

            if firststart <= secondend and firstend >= secondstart:
                Intersection.append([max(firststart,secondstart), min(firstend, secondend)])
            if firstend < secondend:
                first_pointer +=1
            else:
                second_pointer +=1
        return Intersection

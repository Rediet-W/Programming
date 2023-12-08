class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sliced = list(s)
        for space in spaces:
            sliced[space] = " " + sliced[space]
        return ''.join(sliced)
        
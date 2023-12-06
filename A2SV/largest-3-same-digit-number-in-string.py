class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_int=[]
        for i in range(len(num) - 2):
            substring = num[i:i + 3]
            if len(set(substring)) == 1:
                good_int.append(int(substring))

        if len(good_int) > 0:
            good_int.sort()
            max_good = good_int[-1]
            return str(max_good).zfill(3)
        else:
            return ""

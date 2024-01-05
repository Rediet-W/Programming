class Solution:
    def smallestNumber(self, num: int) -> int:
        snum = list(str(abs(num)))
        if num > 0:
            snum.sort()
        else:
            snum.sort(reverse=True)
        if num > 0 and '0' in snum:
            for i in range(1, len(snum)):
                if snum[i] != '0':
                    snum[0], snum[i] = snum[i], snum[0]
                    break
        n = "".join(snum)

        if num < 0:
            return -int(n)
        return int(n)
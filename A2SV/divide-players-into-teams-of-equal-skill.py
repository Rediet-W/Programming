class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        skill.sort()
        start = 0
        end = len(skill)-1
        t = skill[start] + skill[end]
        i = 0
        while start < end:
            if skill[start] + skill[end] == t:
                ans += skill[start] * skill[end]
                i+=1
            start+=1
            end-=1
        if i == len(skill)/2:
            return ans
        return -1
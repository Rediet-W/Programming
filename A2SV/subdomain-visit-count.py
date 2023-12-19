class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        pairs = {}
        for i in cpdomains:
            ls = i.split(" ")
            path = ls[1].split(".")
            for i in range(len(path)):
                c = ".".join(path[i:])
                pairs[c] = pairs.get(c,0) + int(ls[0])
        result = []
        for key, value in pairs.items():
            s = str(value) + " "+ str(key)
            result.append(s)
        return result

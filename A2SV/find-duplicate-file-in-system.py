class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_path= {}
        duplicate={}
        for i in paths:
            split_i = i.split()
            for j in split_i[1:]:
                split_j = j.split("(")
                key, value = split_j[1][::-1], split_i[0] + "/"+ split_j[0]
                if key not in content_path:
                    content_path[key] = set()
                    duplicate[key] = 0
                content_path[key].add(value)
                duplicate[key] +=1
        answer = []
        for key,value in content_path.items():
            if duplicate[key] > 1:
                answer.append(value)
        return answer

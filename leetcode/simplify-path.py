class Solution:
    def simplifyPath(self, path: str) -> str:
        stack =  []
        path = path.split('/')
        for i in path:
            if i == "":
                pass
            else:
                if i == "..":
                    if len(stack):
                        stack.pop()
                elif i == ".":
                    pass
                else:
                    stack.append(i)
            
        return "/" + "/".join(stack)

                
class Solution:
    def valid(self, ls):
            stack = []
            for i in ls:
                if i == "(":
                    stack.append(i)
                else:
                    if not stack or stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
            if len(stack) == 0:
                return True
            else:
                return False
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def parenthesis( curr):
            if len(curr) == 2*n:
                if self.valid(curr):
                    ans.append("".join(curr))

            if len(curr) >= 2*n:
                return
            

            curr.append("(")
            parenthesis( curr)
            curr.pop()

            curr.append(")")
            parenthesis( curr)
            curr.pop()
        parenthesis([])

        return ans
        
                        

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', "-",'*',"/"]
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if i== operators[0]:
                    stack.append(str(a+b))
                elif i == operators[1]:
                    stack.append(str(b-a))
                elif i == operators[2]:
                    stack.append(str(b*a))
                else:
                    if ((a<0 and b>0) or (b<0 and a >0)) and b%a != 0:
                        stack.append(str(b//a+1))
                    else:
                        stack.append(str(b//a))
        a = "".join(stack)
        return int(a)
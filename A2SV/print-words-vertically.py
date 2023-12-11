class Solution:
    def printVertically(self, s: str) -> List[str]:
        ls = s.split(" ")
        longest_word = 0
        for i in ls:
            longest_word = max(longest_word, len(i))
        vertical = []
        bool1 = False
        for i in range(longest_word):
            space = ""
            output = ""
            for j in range(len(ls)):
                if len(ls[j]) <= i:
                    if bool1 == False:
                        output= " " + output
                    else:
                        space = space + " "
                else:
                    if space != "":
                        output+=space
                        space = ""
                    output = output + ls[j][i]
                    bool1 = True 
            vertical.append(output)
        return vertical
        
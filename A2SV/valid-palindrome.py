class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalnum():
                word+=i.lower()
            
        print(word)
        l = 0
        r = len(word) -1
        while l<=r:
            if word[l] != word[r]:
                return False
            l+=1
            r-=1
        return True
        
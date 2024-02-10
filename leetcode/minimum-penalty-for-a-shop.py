class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y = 0
        for i in customers:
            if i == 'Y':
                y += 1
        
        res = y
        idx = 0
        p = y
        for hour in range(len(customers)):
            if customers[hour] == 'N':
                p+=1
            if customers[hour] == 'Y':
                p-=1
            if p < res :
                idx = hour+ 1
                res= p
        return idx


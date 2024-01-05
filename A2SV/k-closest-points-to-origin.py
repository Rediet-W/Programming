class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pt_dis =[]
        for x,y in points:
            dis = x**2 + y**2
            pt_dis.append([[x,y], dis])
        pt_dis.sort(key=lambda x: x[1])
        ans = []
        for i in range(k):
            ans.append(pt_dis[i][0])
        return ans
        
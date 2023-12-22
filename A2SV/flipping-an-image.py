class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        d = {0:1, 1:0}
        for i in range(len(image)):
            s = 0
            e = len(image[i]) - 1
            while s<= e:
                if image[i][s] == image[i][e]:
                    image[i][s] = d.get(image[i][s])
                    image[i][e] = d.get(image[i][e])
                s+=1
                e-=1
            if len(image[i]) %2 !=0:
                mid = len(image[i])//2
                image[i][mid] = d.get(image[i][mid])
        return image

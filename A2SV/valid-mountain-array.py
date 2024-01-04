class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc = False
        dec = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                if inc == False:
                    return False
                    # because it dec w/o inc
                dec = True
            elif arr[i] < arr[i+1]:
                if dec == True:
                    return False #bc I only want one mountain
                inc = True
            else:
                return False
        if inc and dec:
            return True
        else:
            return False       
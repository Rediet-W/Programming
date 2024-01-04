class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        one , two = 0, 0
        ans = []
        while one< len(nums1) and two< len(nums2):
            if nums1[one] == nums2[two]:
                ans.append(nums1[one])
                one +=1
                two +=1
            elif nums1[one] > nums2[two]:
                two +=1
            else:
                one +=1
        return ans


        

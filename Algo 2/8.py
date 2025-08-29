from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        counter = defaultdict(int)

        # nums1 is smaller
        for num in nums1:
            counter[num] += 1
        res = []
        for num in nums2:
            if counter[num] > 0:
                res.append(num)
                counter[num] -= 1

        return res            


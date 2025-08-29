from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    # j += 1
                    # k -= 1
                    while j < k and nums[j] == nums[j+1]:
                        j += 1

                    while k > j and nums[k] == nums[k-1]:
                        k -= 1

                if nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return res            



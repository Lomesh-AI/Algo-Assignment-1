from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        start = -1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                start = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        if start == -1:
            return [-1, -1]
    
        l = 0
        r = n-1
        end = -1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                end = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1 

        return [start, end]


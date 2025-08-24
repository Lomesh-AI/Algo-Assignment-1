class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
        
        last_min_idx = -1
        last_max_idx = -1
        out_of_bound = -1
        count = 0

        for j in range(len(nums)):

            if not mink <= nums[j] <= maxk:
                last_min_idx = -1
                last_max_idx = -1
                out_of_bound = j
                continue

            if nums[j] == mink:
                last_min_idx = j
            if nums[j] == maxk:
                last_max_idx = j 

            if last_min_idx != -1 and  last_max_idx != -1:
                count += min(last_min_idx, last_max_idx) - out_of_bound

        return count               
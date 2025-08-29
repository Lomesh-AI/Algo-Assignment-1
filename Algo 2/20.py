from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1:
            return False

        mapp = {0:-1}
        prefixSum = 0

        for i in range(n):
            prefixSum += nums[i]

            if prefixSum%k in mapp:
                if i - mapp[prefixSum%k] + 1 > 2:
                    return True
            else:
                mapp[prefixSum%k] = i

        return False                      

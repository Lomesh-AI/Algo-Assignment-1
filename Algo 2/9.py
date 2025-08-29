class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] > 1:
            return False

        if nums[n-1] < n-2:
            return False

        for i in range(1, n-1):
            if nums[i] > i + 1 or nums[i] < i-1:
                return False

        return True                

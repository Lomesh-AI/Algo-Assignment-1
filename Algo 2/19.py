class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        n = len(nums)

        while i < n:
            right_position = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[right_position]:
                nums[i], nums[right_position] = nums[right_position], nums[i]
            else:    
                i += 1

        i = 0
        j = 1
        while i < n:
            if nums[i] > 0:
                if nums[i] == j:
                    j += 1
                else:
                    return j
            i += 1      
        return j   

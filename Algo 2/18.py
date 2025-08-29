class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = set()

        i = 0
        while i < len(nums):
            right_position = nums[i] - 1
            if nums[i] != nums[right_position]:
                nums[i], nums[right_position] = nums[right_position], nums[i]
            elif nums[i] == nums[right_position] and i != right_position:
                res.add(nums[i])
                i += 1
            else:
                i += 1  

        return list(res)        


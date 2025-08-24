class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        prefixMin = [0]*n
        prefixMin[0] = nums[0]
        
        for i in range(1, n):
            prefixMin[i] = min(nums[i], prefixMin[i-1])

        for j in range(n-1, 0, -1):
            if nums[j] > prefixMin[j-1]:
                while stack and stack[-1] <= prefixMin[j-1]:
                    stack.pop()

                if stack and stack[-1] < nums[j]:
                    return True

            stack.append(nums[j])

        return False                
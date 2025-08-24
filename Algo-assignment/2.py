class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        n = len(nums)
        stack = []
        for j in range(n):
            while stack and stack[-1] > nums[j] and k > 0:
                stack.pop()
                k -= 1
            stack.append(nums[j])

        while k > 0:
            stack.pop()
            k -= 1

        string = ''.join(stack).lstrip('0')
        return string if string else '0'

        
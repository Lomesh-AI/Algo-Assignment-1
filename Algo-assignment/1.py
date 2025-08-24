class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()
        return not stack
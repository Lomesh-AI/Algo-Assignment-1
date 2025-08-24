class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maxArea = 0

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                ind = stack.pop()
                nse = i
                pse = -1 if not stack else stack[-1]
                maxArea = max(maxArea, heights[ind]*(nse-pse-1))
            stack.append(i)


        # sum indices are still left to cover
        while stack:
            ind = stack.pop()
            nse = n
            pse = -1 if not stack else stack[-1]
            maxArea = max(maxArea, heights[ind]*(nse-pse-1))

        return maxArea
                
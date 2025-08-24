class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        # left pass
        leftsum = [0]*n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            pse = -1
            if stack:
                pse = stack[-1]

            count = i - pse

            prev_sum = 0
            if pse != -1:
                prev_sum = leftsum[pse]

            leftsum[i] = prev_sum + count * heights[i]

            stack.append(i)

        # right pass
        rightsum = [0]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            nse = n
            if stack:
                nse = stack[-1]

            count = nse - i

            next_sum = 0
            if nse < n:
                next_sum = rightsum[nse]

            rightsum[i] = next_sum + count * heights[i]

            stack.append(i)     

        maxx = float('-inf')
        for i in range(n):
            maxx = max(maxx, leftsum[i] + rightsum[i] - heights[i])

        return maxx    






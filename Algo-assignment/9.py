class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []
        total = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                index = stack.pop()
                nge = i
                if stack:
                    pge = stack[-1]
                    width = nge - pge - 1
                    total += (min(height[pge], height[nge]) - height[index]) * width
            stack.append(i) 
        return total     

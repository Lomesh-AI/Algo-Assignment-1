class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def helper(heights):
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

        maxArea = 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0]*cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            area = helper(heights)        
            maxArea = max(maxArea, area)

        return maxArea
        
                
            
        
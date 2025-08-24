class Solution:
    def maximumSumOfHeights(self, arr: List[int]) -> int:
        
        n = len(arr)
        maxx = float('-inf')
        for i in range(n):

            rightsum = arr[i]
            last = arr[i]
            for j in range(i+1, n):
                if last >= arr[j]:
                    last = arr[j]
                rightsum += last

            leftsum = arr[i]
            last = arr[i]
            for j in range(i-1, -1, -1):
                if last >= arr[j]:
                    last = arr[j]
                leftsum += last
            
            maxx = max(maxx, rightsum + leftsum - arr[i])

        return maxx    

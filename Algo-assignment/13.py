from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:        
        dq = deque()
        n = len(nums)
        maxarray = []
        for j in range(n):   
            while dq and dq[-1] < nums[j]:
                dq.pop()
            dq.append(nums[j])

            if j >= k and nums[j-k] == dq[0]:
                dq.popleft()

            if j>=k-1:
                maxarray.append(dq[0])
        return maxarray                

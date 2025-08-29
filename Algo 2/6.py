from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1

        def count_flowers(days, k, m):
            count = 0
            summ = 0

            for i in range(n):
                if bloomDay[i] <= days:
                    summ += 1
                else:
                    summ = 0
                if summ == k:
                    count += 1
                    summ = 0 
            return count >= m        


        l = min(bloomDay)
        r = max(bloomDay)
        ans = 0
        while l <= r:
            mid = l + (r-l)//2
            if count_flowers(mid, k, m):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans            

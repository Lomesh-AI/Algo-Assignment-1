class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def summ(index, m):
            if m <= index:
                return ((m-1)*m)//2 + (index-m+1)
            return ((m-1)*m)//2 - ((m-index)*(m-index-1))//2 

        l = 1
        h = maxSum
        ans = float('-inf')
        while l <= h:
            mid = l + (h-l)//2
            total_sum = summ(index, mid) + mid + summ(n-index-1, mid)

            if total_sum <= maxSum:
                ans = mid
                l = mid + 1
            else:
                h = mid - 1

        return ans            
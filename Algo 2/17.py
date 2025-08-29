class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        total_pairs = (n*(n-1))//2
        count_good_pairs = 0
        mapp = {}
        for i in range(n):
            d = nums[i] - i
            if d not in mapp:
                mapp[d] = 1
            else:
                count_good_pairs += mapp[d]
                mapp[d] += 1    

        return total_pairs - count_good_pairs        


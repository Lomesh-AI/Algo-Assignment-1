class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                summ1 = nums[a] + nums[b]

                c = b + 1
                d = n-1
                # print(target)
                while c < d:
                    totalsumm = summ1 + nums[c] + nums[d]
                    if totalsumm == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c+1]:
                            c += 1
                        while d >c and nums[d] == nums[d-1]:
                            d -= 1    

                    if totalsumm < target:
                        c += 1
                    else:
                        d -= 1
        return res                    

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        res = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n-1

            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                diff2 = abs(target - summ)


                if diff > diff2:
                    ans = summ
                    diff = diff2
                
                if summ == target:
                    return summ
                elif summ > target:
                    k -= 1
                else:
                    j += 1        

        return ans                

                    


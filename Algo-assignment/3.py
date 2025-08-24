class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        pair = []
       
        for ind, val in enumerate(nums):
            pair.append((val, ind))

        def merge(left, mid, right):
            nonlocal ans, pair

            temp = [] # right - left + 1
            i = left
            j = mid + 1

            while i<=mid and j <= right:
                if pair[i][0] <= pair[j][0]:
                    temp.append(pair[j])
                    j += 1
                else:
                    temp.append(pair[i])
                    ans[pair[i][1]] += right - j + 1 #starting from j and till right all will be smaller than i
                    i += 1  

            while i <= mid:
                temp.append(pair[i])
                i += 1
            while j <= right:
                temp.append(pair[j])
                j += 1

            for k in range(left, right+1):
                pair[k] = temp[k-left]                  

        def merge_sort(left, right):
            if left >= right:
                return
            mid = left + (right-left)//2
            merge_sort(left, mid)
            merge_sort(mid+1, right)
            merge(left, mid, right)                

        merge_sort(0, n-1)
        return ans    
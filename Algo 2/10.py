class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        def merge_sort(l, r):
            if l >= r:
                return 
            mid = l + (r-l)//2    
            merge_sort(l, mid)
            merge_sort(mid+1, r)
            merge(l, mid, r)

        def merge(l , mid, r):
            nonlocal count
            i = l
            j = mid+1
            temp = []
            while i <= mid and j <= r:
                if nums[i] > 2*nums[j]:
                    count += mid-i+1
                    j += 1
                else:
                    i += 1

            i = l
            j = mid+1  
            while i<= mid and j <= r:
                if nums[i] > nums[j]:
                    temp.append(nums[j])
                    j += 1
                else:
                    temp.append(nums[i])
                    i += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= r:
                temp.append(nums[j])
                j += 1

            for i in range(r-l+1):
                nums[l+i] = temp[i]   

        merge_sort(0, len(nums)-1)
        return count                                  


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (m+n+1)//2
        l = 0  
        h = min(k, n)
        while l <= h:
            mid1 = l + (h-l)//2
            mid2 = k - mid1

            r1 = nums1[mid1] if mid1 < n else float('inf')
            l1 = nums1[mid1-1] if mid1 > 0 else float('-inf')

            r2 = nums2[mid2] if mid2 < m else float('inf')
            l2 = nums2[mid2-1] if mid2 > 0 else float('-inf')

            if l1 <= r2 and l2 <= r1:
                if (n+m)%2==0:
                    return (max(l1, l2) + min(r1, r2))/2
                return max(l1, l2)   
            if l1 > r2:
                h = mid1 - 1
            else:
                l = mid1 + 1    

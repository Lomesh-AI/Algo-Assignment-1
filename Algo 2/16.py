class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        res = []
        min_heap = []

        for i in range(min(len(nums2), k)):
            min_heap.append([nums1[0]+nums2[i], 0, i])
        
        while k > 0 and min_heap:
            summ, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            k -= 1

            if i+1 < len(nums1):
                heapq.heappush(min_heap, [nums1[i+1]+nums2[j], i+1, j])

        return res      
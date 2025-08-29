from typing import List
class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        if n<2:
            return arr[0]
            
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n-1] != arr[n-2]:
            return arr[n-1]

        l = 1
        r = n - 2


        while l <= r:
            mid = l + (r-l)//2

            if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
                return arr[mid]

            if mid%2==0:
                if arr[mid] == arr[mid+1]:
                    l = mid + 1

                elif arr[mid] == arr[mid-1]:
                    r = mid - 1

            else:
                if arr[mid] == arr[mid+1]:
                    r = mid - 1
                elif arr[mid] == arr[mid-1]:
                    l = mid + 1
        # print(l)
        return arr[mid]                                               
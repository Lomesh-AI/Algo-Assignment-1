from collections import deque
from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.minHeap = SortedList()
        self.maxHeap = SortedList()
        self.middle = SortedList()
        self.q = deque([])
        self.m = m
        self.k = k
        
    def addElement(self, num: int) -> None:
        self.q.append(num)

        if not self.minHeap or num < self.minHeap[-1]:
            self.minHeap.add(num)
        elif not self.maxHeap or num > self.maxHeap[0]:
           self.maxHeap.add(num)
        else:
            self.middle.add(num)

        if len(self.q) > self.m:
            to_remove = self.q.popleft()
            if to_remove <= self.minHeap[-1]:
                self.minHeap.remove(to_remove)
            
            elif to_remove >= self.maxHeap[0]:
                self.maxHeap.remove(to_remove)

            else:
                self.middle.remove(to_remove)

        while len(self.minHeap) > self.k:
            ele = self.minHeap.pop()
            self.middle.add(ele)
        
        while len(self.maxHeap) > self.k:
            ele = self.maxHeap.pop(0)
            self.middle.add(ele)

        while len(self.minHeap) < self.k and self.middle:
            ele = self.middle.pop(0)
            self.minHeap.add(ele)

        while len(self.maxHeap) < self.k and self.middle:
            ele = self.middle.pop(-1)
            self.maxHeap.add(ele)   

        if self.minHeap and self.middle and self.minHeap[-1] > self.middle[0]:
            minn = self.minHeap.pop(-1)
            mid = self.middle.pop(0)
            self.minHeap.add(mid)
            self.middle.add(minn)

        if self.maxHeap and self.middle and self.maxHeap[0] < self.middle[-1]:
            maxx = self.maxHeap.pop(0)
            mid = self.middle.pop(-1)
            self.maxHeap.add(mid)
            self.middle.add(maxx)
            
    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1

        if len(self.middle) == 0:
            return 0

        return sum(self.middle)//(self.m-2*self.k)        
        
        

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
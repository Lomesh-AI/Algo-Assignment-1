class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.arr = [value] + self.arr
            return True
        return False    
        
    def insertLast(self, value: int) -> bool:
        if not self.isFull():   
            self.arr += [value]
            return True
        return False    

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            del self.arr[0]
            return True
        return False    

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            del self.arr[-1]
            return True
        return False

    def getFront(self) -> int:
        return self.arr[0] if self.arr else -1

    def getRear(self) -> int:
        return self.arr[-1] if self.arr else -1
        
    def isEmpty(self) -> bool:
        return not self.arr

    def isFull(self) -> bool:
        return len(self.arr) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
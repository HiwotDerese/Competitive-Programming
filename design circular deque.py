class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None]*k
        self.Maxsize = k
        self.size = 0
        self.head = 0
        self.tail = 0
        
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.deque[self.head] = value
            self.size += 1
            return True
        else:
            self.head = (self.head - 1)%self.Maxsize
            self.deque[self.head] = value
            self.size += 1
            return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.deque[self.tail] = value
            self.size += 1
            return True
        else:
            self.tail = (self.tail + 1)% self.Maxsize
            self.deque[self.tail] = value
            self.size += 1
            return True
        
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque[self.head] = None
            if self.size == 1:
                self.size -=1
                return True
            else:
                self.head = (self.head + 1)% self.Maxsize
                self.size -=1
                return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque[self.tail] = None
            if self.size == 1:
                self.size -=1
                return True
            else:
                self.tail = (self.tail - 1)% self.Maxsize
                self.size -=1
                return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.head]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.tail]

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False
        

    def isFull(self) -> bool:
        return True if self.size == self.Maxsize else False
        


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
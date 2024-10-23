class MyCircularDeque:

    def __init__(self, k: int):
        self.tail = k-1
        self.head = 0
        self.n = 0
        self.arr = [0]*k
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head-1) % self.k
        self.arr[self.head] = value
        self.n += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail+1) % self.k
        self.arr[self.tail] = value
        self.n += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head+1) % self.k
        self.n -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail-1) % self.k
        self.n -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.tail]

    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.n == self.k

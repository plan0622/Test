from .fifo import FIFO
from .fifo import Node


class Stack(FIFO):
    def __init__(self, max_length):
        FIFO.__init__(self, max_length)

    def push(self, data):
        lastNode = self.tail.prev
        newNode = Node()
        newNode.data = data

        lastNode.next = newNode
        newNode.prev = lastNode

        newNode.next = self.tail
        self.tail.prev = newNode
        self.length += 1

    def pop(self):
        assert len(self) > 0
        lastNode = self.tail.prev
        parentNode = lastNode.prev

        parentNode.next = self.tail
        self.tail.prev = parentNode
        self.length -= 1

        return lastNode.data

    def __iter__(self):
        assert len(self) > 0

        nodePtr = self.tail.prev
        while nodePtr != self.head:
            yield nodePtr.data
            nodePtr = nodePtr.prev


if __name__ == "__main__":
    s = Stack(100)
    s.push(1)
    s.push(2)
    s.push(3)

    print("Pop up the last element %d" % (s.pop()))
    for x in s:
        print(x)

import collections
class MyStack:
    def __init__(self):
        self.stack = []
        # 采用队列的思想就可以了
        # self.stack =collectins.deque()

    def push(self, x: int) -> None:
        self.stack.insert(0, x)

    def pop(self) -> int:
        for i in range(len(self.stack)-1):
            self.stack.insert(0, self.stack.pop())
        return self.stack.pop()

    def top(self) -> int:
        tmp = self.pop()
        self.stack.insert(0, tmp)
        return tmp

    def empty(self) -> bool:
        return not self.stack

a = MyStack()
a.push(1)
a.push(2)
print(a.top())
a.pop()
print(a.top())


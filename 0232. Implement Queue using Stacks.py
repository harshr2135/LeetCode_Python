class MyQueue:

    def __init__(self):
        self.stack = []
        self.height = 0 

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.height += 1

    def pop(self) -> int:
        if self.height == 0:
            return None

        top = self.stack[0]
        self.stack = self.stack[1:]
        self.height -= 1
        return top

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return self.height == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
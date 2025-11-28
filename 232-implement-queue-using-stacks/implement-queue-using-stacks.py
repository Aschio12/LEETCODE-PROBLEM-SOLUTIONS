class MyQueue:

    def __init__(self):
        self.sin=[]
        self.sout=[]

    def push(self, x: int) -> None:
        self.sin.append(x)
    def pop(self) -> int:
        if not self.sout:
            while self.sin:
                self.sout.append(self.sin.pop())
        return self.sout.pop()
    def peek(self) -> int:
        if not self.sout:
            while self.sin:
                self.sout.append(self.sin.pop())
        return self.sout[-1]

    def empty(self) -> bool:
        return not self.sout and not self.sin


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
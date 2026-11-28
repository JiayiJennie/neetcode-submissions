class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = -2^31

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minval = min(self.minval, val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

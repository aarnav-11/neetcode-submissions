class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        ret = self.stack[-1]
        self.stack.pop()
        self.minstack.pop()
        return ret

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

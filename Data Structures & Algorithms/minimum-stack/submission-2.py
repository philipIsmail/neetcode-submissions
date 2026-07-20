class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else None

mytest = MinStack() # Removed self.
mytest.push(1)      # Removed self.
mytest.push(3)      # Removed self.
mytest.push(7)      # Removed self.
mytest.push(15)     # Removed self.

print(mytest.pop())   # Output: 15 (Now returns the value correctly!)
print(mytest.getMin()) 

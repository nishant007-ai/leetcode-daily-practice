class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

#push(3)
#push(5)
#getMin() → gives 3  (because 3 is the smallest so far)
#push(2)
#push(1)
#getMin() → gives 1  (because 1 is now the smallest)
#pop()
#getMin() → gives 2  (because after removing 1, 2 is the next smallest)

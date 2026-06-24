class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            current_min = self.minStack[-1] 
            if val < current_min:
                self.minStack.append(val)
            else:
                self.minStack.append(current_min)
        



        

    def pop(self) -> None:
        if self.mainStack :
            self.mainStack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if self.mainStack :
            return self.mainStack[-1]

    def getMin(self) -> int:
        if self.minStack :
            return self.minStack[-1]

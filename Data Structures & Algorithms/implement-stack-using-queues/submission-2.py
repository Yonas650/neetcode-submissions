class MyStack:

    def __init__(self):
        self.q=deque()
        self.size=0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.size+=1
    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(self.size-1):
            poped=self.q.popleft()
            self.q.append(poped)
        
        self.size-=1
        return self.q.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        s_top=self.pop()
        self.push(s_top)
        return s_top


    def empty(self) -> bool:
        return  self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
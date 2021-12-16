# 232.用栈实现队列
# 请你仅使用两个栈实现先入先出的队列。队列应当支持一般队列支持的所有操作。
# 解题思路
# 1.典型的数据结构题，用两个栈来实现，一个顺序栈一个逆序栈来弥补栈不能直接弹出队首的缺点。其
# 余优先输出逆序栈后输出殊顺序栈。


class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x: int) -> None:
        self.stack1.append(x)
        
    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        return self.stack2[-1] if self.stack2 else self.stack1[0]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


obj = MyQueue()

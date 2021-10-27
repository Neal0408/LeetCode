# Offer.59-2 队列的最大值
# 请定义一个队列并实现函数 max_value 得到队列里的最大值,要求函数 max_value, push_back,
# pop_front 的均摊时间复杂度都是 O(1).
# 解题思路
# 最开始是想到说用一个变量把最大值存储下来,这样返回最大值的时候就可以直接获取并返回,时间复杂
# 度是 O(1),但是做着做着发现在 pop 的时候弹出完最大值之后还需要第二大值去代替它的位置,所以
# 就想到用单调队列去存储最大值列了.
import queue


class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


obj = MaxQueue()

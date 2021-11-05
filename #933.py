# 933.最近的请求次数
# 写一个 RecentCounter 类来计算特定时间范围内最近的请求.
# 解题思路
# 原本还在想这道题那里要用到队列,提交后才发现超时了.把 request 做成队列超过范围的就弹出,这
# 样就不用重复操作了.自己做的时候出现了个 deque 变异报错想应该是 for 循环的时候队列发生了变
# 化,当时为了解决就临时用了个笨方法把原队列保存了.但是后来想了一下完全没有必要,直接 while 循
# 环队首元素不符合直接左弹出就可以了.这样时间上就会快很多.
from collections import deque


class RecentCounter:

    def __init__(self):
        self.count = 0
        self.request = deque()

    # 最开始做的,超时了
    def ping1(self, t: int) -> int:
        self.request.append(t)
        count = 0
        for i in self.request:
            if self.request[-1] - 3000 <= i <= self.request[-1]:
                count += 1
        return count

    # 因为循环的时候出现 deque 变异错误,所以用了个笨方法 copy 了原队列.后来想了一下并不需要.
    def ping2(self, t: int) -> int:
        self.request.append(t)
        temp = self.request.copy()
        for i in temp:
            if i < self.request[-1] - 3000:
                self.request.popleft()
        return self.request.__len__()

    def ping(self, t: int) -> int:
        self.request.append(t)
        while self.request[0] < t - 3000:
            self.request.popleft()
        return len(self.request)


obj = RecentCounter()

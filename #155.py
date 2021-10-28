# 155.最小栈
# 设计一个支持 push, pop, top 操作,并能在常数时间内检索到最小元素的栈
# 解题思路
# 1.比较常规的一个数据结构题, 常数时间要求需要注意是否满足条件.自己做的时候最小值搞了个单调
# 列表,当时想了一下如果双端队列确实收尾添加删除操作的时间复杂度都是 O(1) 但是给我感觉像是上
# 了个牛刀,就姑且先用了列表的 insert 来保持列表的单调,但是果然这边不是常数时间, 当时错以为
# O(1) 和 O(n)一样,结果并不是.
# 2.官方解答思路是差不多的只不过更巧妙一点,就是插入值并不比当前栈内最小值还要小的话,到栈内最
# 小值弹出之前,最小值都不会变.
import math


class MinStack1:

    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStack2:

    def __init__(self):
        self.stack = []
        # self.min = None 最小元素 搞个单调列表 有必要上双端队列么 - -  先用列表试试
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        else:
            self.min.insert(0, val)
            # 这个时间复杂度要注意一下 双端队列的话就是 O(1)

    def pop(self) -> None:
        if self.min[-1] == self.stack.pop():
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# s = MinStack2()
s = MinStack1()

# 1381.设计一个支持增量操作的栈
# 请你设计一个支持增量操作的栈。void inc(int k, int val) 栈底的k个元素的值都增加val。如果
# 栈中元素总数小于 k，则栈中的所有元素都增加 val。
# 解题思路
# 1.列表和队列的方法都做过，列表最慢，队列快了一倍，但是都没有好好利用到 maxSize这个条件，所
# 以还是根据官方题解静态数组的方式来做比较好。


class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = [0] * maxSize
        self.add = [0] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top != len(self.stk) - 1:
            self.top += 1
            self.stk[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        ret = self.stk[self.top] + self.add[self.top]
        if self.top != 0:
            self.add[self.top - 1] += self.add[self.top]
        self.add[self.top] = 0
        self.top -= 1
        return ret

    def increment(self, k: int, val: int) -> None:
        lim = min(k - 1, self.top)
        if lim >= 0:
            self.add[lim] += val


obj = CustomStack(3)

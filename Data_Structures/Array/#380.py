# 380.O(1)时间插入、删除和获取随机元素
# 实现 RandomizedSet 类。
# 解题思路
# 1.最开始没有想法，因为总有一个函数是不好实现到题目要求的 O(1)的，然后看了题解。是使用了哈
# 希表 + 链表的组合，这时需要删除的元素与最后一个元素互换后删除就可以达到常数时间。这个思想还
# 是有很多地方需要学习的。
from random import choice


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self):
        return choice(self.list)


obj = RandomizedSet()

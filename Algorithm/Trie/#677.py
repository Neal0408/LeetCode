# 677.键值映射
# 实现一个 MapSum 类，支持两个方法，insert 和 sum。
# 解题思路
# 1.前缀树方法，前缀树主要操作为插入和查询，题目中用到的是插入和求和。插入的时候构造前缀树，
# 固定 Key 的时候赋予值。在求和中先循环到当前前缀，之后 dfs 求 children 的 val 的总和。
class TrieNode:
    
    def __init__(self):
        self.isKey = False
        self.value = 0
        self.children = {}


class MapSum:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.value = val
        node.isKey = True

    def sum(self, prefix: str) -> int:

        def dfs(node):
            if not node:
                return 0
            if node.isKey:
                self.res += node.value
            for key in node.children:
                dfs(node.children[key])

        node = self.root
        self.res = 0
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        dfs(node)
        return self.res


obj = MapSum()

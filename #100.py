# 100.相同的树
# 给你两棵二叉树的根节点 p 和 q,编写一个函数来检验两棵树是否相同.
# 解题思路
# 终于刷到树这边了,这道题是考察怎么遍历树.有深度优先搜索和广度优先搜索.但是我更在意的是怎么用
# 数组创建一棵树,翻看了一下力扣源码还是有很多参考价值的.


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


obj = Solution()

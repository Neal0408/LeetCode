# 剑指 Offer 32-3.从上到下打印二叉树3
# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的
# 顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
# 解题思路
# 1.层序遍历，BFS。跟之前几个倒是没啥区别，这题就需要识别一下奇偶层倒序添加temp就可以了。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp[::-1] if len(res) % 2 else temp)
        return res


obj = Solution()

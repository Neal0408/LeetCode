# 剑指 Offer 32-1.从上到下打印二叉树
# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
# 解题思路
# 1.层序遍历，广度优先搜索BFS。如果已经意识到是BFS了后面就很好写了。这边需要注意的是如果节点
# 为空时返回的需要是空列表而不是None，这个提交后样例没通过后需要小小的改动。


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


obj = Solution()

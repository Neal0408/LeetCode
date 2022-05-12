# 剑指 Offer 32-2.从上到下打印二叉树2
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
# 解题思路
# 1.层序遍历，广度优先搜索BFS。跟32-1没什么区别。按层输出。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
            res.append(temp)
        return res


obj = Solution()

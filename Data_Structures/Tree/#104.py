# 104.二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 解题思路
# 1.自底向上，当前高度的定义是取左右子树高度的最大值加一。终止条件是在没有元素遍历了即为终止。
# 相当于后序遍历。
# 2.自顶向下，相当于前序遍历。因为要额外维护一个类变量。
# 3.BFS广度优先遍历，也是层序遍历。一层一层遍历到最后高度就是深度。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 自底向上。递归。
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        return max(leftHeight, rightHeight) + 1

    # 自顶向下。遍历。
    def dfs(self, root, cur):
        if not root:
            return 0
        cur += 1
        if not root.left and not root.right:
            self.depth = max(self.depth, cur)
        self.dfs(root.left, cur)
        self.dfs(root.right, cur)
        return self.depth

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        cur = 0
        self.depth = 0
        return self.dfs(root, cur)

    # 层序遍历。
    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 0

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth


obj = Solution()

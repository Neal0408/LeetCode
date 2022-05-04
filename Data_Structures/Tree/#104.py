# 104.二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 解题思路
# 1.自底向上，当前高度的定义是取左右子树高度的最大值加一。终止条件是在没有元素遍历了即为终止。
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        return max(leftHeight, rightHeight) + 1


obj = Solution()

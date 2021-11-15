# 110.平衡二叉树
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 解题思路
# 1.平衡二叉树的定义是每个节点的左右子树的高度差的绝对值不超过1，根据这个求树的高度然后计算高
# 度差。自顶向下的递归。
# 2.自底向上的递归。方法一会对同一个节点反复调用函数从而导致时间复杂度较高。二叉树类的问题还
# 是需要多去调试来明白递归的过程。调试的时候加个文本缩进看着会更方便一些。


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced2(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


obj = Solution()

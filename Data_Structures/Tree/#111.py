# 111.二叉树的最小深度
# 给定一个二叉树，找出其最小深度。
# 解题思路
# 1.自底向上，递归方法。分别算出左右子树高度，取小的那个加1。若有一侧子树为空则返回另一侧加1。
# 2.层序遍历。


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)
        return min(leftHeight, rightHeight) + 1 if leftHeight != 0 and rightHeight != 0 else max(leftHeight, rightHeight) + 1
    
    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 1
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth


obj = Solution()

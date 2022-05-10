# 112.路径总和
# 给你二叉树的根节点root和一个表示目标和的整数targetSum。
# 解题思路
# 1.递归。假定从根节点到当前节点的值之和为val，则是否从当前节点的子节点到子节点的路径，满足其
# 路径之和为sum - val。把大问题转化为小问题做递归。最后需要判断是否为叶子节点即左右孩子节点均
# 为空。
# 2.层序遍历。利用队列来存储当前层的节点，和到当节点的总和。


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        que_node = [root]
        que_val = [root.val]
        while que_node:
            node = que_node.pop(0)
            val = que_val.pop(0)
            if not node.left and not node.right:
                if val == targetSum:
                    return True
                continue
            if node.left:
                que_node.append(node.left)
                que_val.append(node.left.val + val)
            if node.right:
                que_node.append(node.right)
                que_val.append(node.right.val + val)
        return False


obj = Solution()

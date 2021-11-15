# 101.对称二叉树
# 给定一个二叉树,检查它是否是镜像对称的.
# 解题思路
# 1.想想怎么表达左子树和右子树.递归的终止条件有三个,一左右节点都为空,二俩节点中其中一个为空,
# 三俩个节点的值不相等.再递归比较其左节点的左孩子和右节点的右孩子以及左节点的右孩子和右节点的
# 左孩子是否相同.
# 2.还有一种做法就是用队列去做,把根的左右节点插入到队列中,比较这两个节点.


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(left, right):
            if not (left or right):
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)

    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root or not (root.left or root.right):
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)

            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)
        return True


obj = Solution()

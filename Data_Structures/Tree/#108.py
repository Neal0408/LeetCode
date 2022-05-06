# 108.将有序数组转换为二叉搜索树
# 给你一个整数数组nums，其中元素已经按升序排列，请你将其转换为一棵高度平衡二叉搜索树。
# 解题思路
# 1.二叉树的一个特点就是中序遍历必然有序，所以找准根节点位置左侧区间是左子树右侧区间是右子树。
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(nums) - 1)


obj = Solution()

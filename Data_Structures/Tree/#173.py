# 173.二叉搜索树迭代器
# 实现一个二叉搜索树迭代器类BSTIterator，表示一个按中序遍历二叉搜索树BST的迭代器。
# 解题思路
# 1.把中序遍历的结果全部入队列，这是比较常规的做法。
# 2.单调栈的方法。先所有节点的左孩子都入栈，弹出后判断右孩子是否存在，存在则入栈。再把右孩子
# 的所有左孩子节点入栈。
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = collections.deque()
        self.inOrder(root)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.queue.append(root.val)
        self.inOrder(root.right)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue) > 0


class BSTIterator2:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack.pop()
        node = cur.next
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


obj = BSTIterator(TreeNode())
obj2 = BSTIterator2(TreeNode())

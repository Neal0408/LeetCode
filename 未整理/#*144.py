# Definition for a binary tree node.
import json
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root.
        res = []
        self.preOrder(root, res)

        return res

    def preOrder(self, root, res):
        if not root:
            return res
        res.append(root.val)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)

        return res


def stringToTreeNode(input):
    # input = input.strip()
    # input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


if __name__ == '__main__':
    # main()
    root = stringToTreeNode('1, null, 2, 3')
    ret = Solution().preorderTraversal(root)
    out = integerListToString(ret)
    print(out)


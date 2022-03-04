# 150.逆波兰表达式求值
# 根据逆波兰表示法，求表达式的值。
# 解题思路
# 1.用栈作为辅助，遇到数字入栈，遇到符号出栈两个元素运算完后入栈。
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        dic = {'+', '-', '*', '/'}
        res = []
        for i in tokens:
            if i not in dic:
                res.append(i)
            elif i == '+':
                B = int(res.pop())
                A = int(res.pop())
                res.append(A + B)
            elif i == '-':
                B = int(res.pop())
                A = int(res.pop())
                res.append(A - B)
            elif i == '*':
                B = int(res.pop())
                A = int(res.pop())
                res.append(A * B)
            elif i == '/':
                B = int(res.pop())
                A = int(res.pop())
                res.append(A / B)
        return int(res[0])


obj = Solution()

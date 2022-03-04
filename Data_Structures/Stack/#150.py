# 150.逆波兰表达式求值
# 根据逆波兰表示法，求表达式的值。
# 解题思路
# 1.用栈作为辅助，遇到数字入栈，遇到符号出栈两个元素运算完后入栈。
from typing import List
import operator


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y),
        }
        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op[token](num1, num2)
            finally:
                stack.append(num)

        return stack[0]


obj = Solution()

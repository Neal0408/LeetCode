# 227.基本计算器2
# 给你一个字符串表达式，请你实现一个基本计算器来计算并返回它的值。
# 解题思路
# 1.原本是想用两个栈一个栈用来记符号一个用来记数字，但是还需要考虑符号优先级这个事情就比较复
# 杂，没写出来。


class Solution:

    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preSign = s[i]
                num = 0
        return sum(stack)
    

obj = Solution()
obj.calculate(" 3+5 / 2 ")

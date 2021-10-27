# 20. 有效的括号
# 给定一个只包括括号的字符串 s,判断字符串是否有效.
# 解题思路
# 第一个冒出来的想法是用栈,左右对应则出栈,栈为空则有效.这样的话就需要一个左右括号的对应关系,
# 设计一个 pairs 字典用来判断右括号的类型,如果栈为空栈底添加元素,如果栈中已经有元素存在则判
# 断其是否与其属于同一类型括号,是则弹出,不是则为无效.


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


obj = Solution()
s1 = '()[]{}'
res = obj.isValid(s1)

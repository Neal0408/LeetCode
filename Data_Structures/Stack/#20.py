# 20.有效的括号
# 给定一个只包括括号的字符串，判断字符串是否有效。
# 解题思路
# 1.典型的栈的应用。用字典做括号的映射关系。


class Solution:

    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


obj = Solution()

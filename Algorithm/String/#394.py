# 394.字符串解码
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 解题思路
# 1.找到中括号对应的东西，但是都不确定找不到找得到。这道题压根不会，不知道从哪里开始下手好。
# 官方题解中第一个方法使用的是辅助站法。
# 2.第二个是用递归法。


class Solution:

    # 方法一 辅助站法
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

    # 方法二 递归法
    def decodeString2(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s, 0)


obj = Solution()

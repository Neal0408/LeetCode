# 剑指 Offer 05.替换空格
# 请实现一个函数，把字符串s中的每个空格替换成"%20"。
# 解题思路
# 1.因为Python中字符串为不可变元素，所以要么用列表，要么用字符串的 replace 方法来替换。


class Solution:

    def replaceSpace(self, s: str) -> str:
        res = []
        for i in s:
            if i == ' ':
                res.append('%20')
            else:
                res.append(i)
        return ''.join(res)


obj = Solution()

# 剑指 Offer 58-2.左旋转字符串
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
# 解题思路
# 1.最简单一点做就是直接切片返回就好了。
# 2.列表遍历拼接。如果面试时候要求不能用切片函数的时候则使用此方法。


class Solution:

    # 方法一 切片法
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

    # 方法二 列表遍历拼接
    def reverseLeftWords2(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)


obj = Solution()

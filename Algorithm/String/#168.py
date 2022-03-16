# 168.Excel表列名称
# 给你一个整数columnNumber，返回它在 Excel 表中相对应的列名称。
# 解题思路
# 1.26为一个进制，进制转换为字母。


class Solution:

    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            a0 = (columnNumber - 1) % 26 + 1
            ans.append(chr(a0 - 1 + ord('A')))
            columnNumber = (columnNumber - a0) // 26
        return "".join(ans[::-1])


obj = Solution()

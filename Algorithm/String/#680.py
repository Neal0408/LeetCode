# 680.验证回文字符串2
# 给定一个非空字符串s，最多删除一个字符。判断是否能称为回文字符串。
# 解题思路
# 1.双指针。从最左端和最右端开始比较字符，如果判断为相等元素就向内移动继续判断是否是回文串，
# 在不同的情况下因为允许可以删除一个元素，判断除去当前元素后剩下两个区间是否构成回文串。


class Solution:

    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True


obj = Solution()

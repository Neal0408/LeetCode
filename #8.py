# 8.字符串转换整数
# 请你来实现一个函数,使其能将字符串转换成一个 32 位有符号整数.
# 解题思路
# 因为这个题只涉及整数部分还算好处理一些, 如果是需要识别到小数部分可能就要用到有限状态机了.


class Solution:

    def myAtoi(self, s: str) -> int:
        s1 = s.strip()
        if not s1: return 0
        res, i, sign = 0, 1, 1
        int_max, int_min, boundary = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if s1[0] == '-': sign = -1
        elif s1[0] != '+': i = 0
        for c in s1[i:]:
            if not '0' <= c <= '9': break
            if res > boundary or res == boundary and c > '7':
                return int_max if sign == 1 else int_min
            res = 10 * res + ord(c) - ord('0')
        return sign * res


obj = Solution()

result = obj.myAtoi("  -123")

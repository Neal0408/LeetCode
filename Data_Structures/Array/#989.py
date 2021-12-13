# 989.数组形式的整数加法
# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
# 解题思路
# 1.自己写是写出来了，但是比较别扭因为最开始写的时候没有考虑到 A 位数更小。思路还是有点局限。
from typing import List


class Solution:

    # 方法一 乱七八糟
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        A = num[::-1]
        B = []
        # 将 k 变数组。
        while k:
            B.append(k % 10)
            k = (k - k % 10) // 10

        # A比 B 短的时候。
        if len(A) < len(B):
            A, B = B, A

        # 把 B加到 A 中。
        for i in range(len(B)):
            A[i] = A[i] + B[i]

        # A 中超过 10 的做进位，超过 A 长度的做列表添加。
        for i in range(len(A)):
            if A[i] >= 10:
                if i < len(A) - 1:
                    A[i + 1] = A[i + 1] + A[i] // 10
                    A[i] = A[i] % 10
                else:
                    A.append(A[i] // 10)
                    A[i] = A[i] % 10

        return A[::-1]

    # 方法二 正规一点的
    def addToArrayForm2(self, num: List[int], k: int) -> List[int]:
        res = []
        i, carry = len(num) - 1, 0
        while i >= 0 or k != 0:
            x = num[i] if i >= 0 else 0
            y = k % 10 if k != 0 else 0

            sum = x + y + carry
            res.append(sum % 10)
            carry = sum // 10

            i -= 1
            k //= 10
        if carry != 0:
            res.append(carry)
        return res[::-1]


obj = Solution()

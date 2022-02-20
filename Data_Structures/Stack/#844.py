# 844.比较含退格的字符串
# 给定s和t两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回true。#代表退
# 格字符。
# 解题思路
# 1.本身问题很简单，各自循环入栈遇到警号出栈最后比较两个是否相等。
# 2.但是额外如果限定O(n)时间复杂度和O(1)的空间复杂度的话怎么做才是主要考察对象。则需要逆序
# 遍历。因为字符会不会被删除只与它之后的字符有关与它之前的字符无关，所以逆序遍历遇到警号就跳
# 一格。


class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s: str) -> str:
            ret = list()
            for ch in s:
                if ch != "#":
                    ret.append(ch)
                elif ret:
                    ret.pop()
            return "".join(ret)

        return build(S) == build(T)

    def backspaceCompare2(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0
        while i >= 0 or j >=0:
            while i >= 0:
                if S[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[i]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1

        return True


obj = Solution()

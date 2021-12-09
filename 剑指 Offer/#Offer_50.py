# 剑指 Offer 50.第一个只出现一次的字符
# 在字符串 s 中找出第一个只出现一次的字符。如果没有。返回一个单空格。s 只包含小字符。
# 解题思路
# 1.最开始有点被题目的相关标签误导了，标签有队列，想着必须要用队列做啊什么的，后来试了发现队
# 列并不是很方便。然后重新思考了一下，用哈希来记录出现与否，列表记录顺序。应该算比较常规做法。
# 2.跟题解思路差不多，但很惊讶的是 Python3.6 开始字典已经是有序的了。


class Solution:

    # 方法一 集合和列表
    def firstUniqChar(self, s: str) -> str:
        dic = set()
        res = []
        for i in s:
            # 不存在集合中则添加
            if i not in dic:
                dic.add(i)
                res.append(i)
            # 存在集合中也存在列表中表明这是第二次遇到这个元素
            elif i in res:
                res.remove(i)
            # 已经出现多次就跳过
            else:
                continue
        if not res:
            return ' '
        else:
            return res[0]

    # 方法二 有序哈希表
    def firstUniqChar2(self, s: str) -> str:
        dic = {}
        for c in s:
            # 直接用not c in dic，也是正常的只不顾 PEP8 会警告。烦人的 PEP8 - -！
            dic[c] = not(c in dic)
        for k, v in dic.items():
            if v:
                return k
        return ' '


obj = Solution()

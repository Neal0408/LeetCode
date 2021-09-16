# 7.整数反转
# 32位有符号整数x,返回x中的数字部分反转后的结果,如果超过32位范围就返回0
# 解题思路,又看错题了,是反转过后判断超不超范围,因为本身给的就是32位不会超范围
# 将int转换为str,因为str可以切片,就可以切片倒序输出,输出之前进行判断


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            return 0 if int(str(x)[::-1]) > 2 ** 31 - 1 else int(str(x)[::-1])
        else:
            return 0 if int(str(-x)[::-1]) > 2 ** 31 - 1 else int('-' + str(-x)[::-1])


obj = Solution()
A = -123
result = obj.reverse(A)
print(result)

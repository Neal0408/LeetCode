# 881.救生艇
# 第 i 个人的体重为 people[i]，每艇船可以承载的最大重量为 limit。每艘船最多可以同时载两人，
# 但条件是这些人的重量之和最多为 limit。返回载到每个人所需的最小船数。
# 解题思路
# 1.先进行排序，最轻和最重加起来大于限重则只能重的自己坐船，再来如果他俩之和小于或等于限重则
# 可以两个人一起坐船离开。
from typing import List


class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1
            else:
                light += 1
                heavy -= 1
            ans += 1
        return ans


obj = Solution()

# Problem: LeetCode 1. Two Sum
# Approach: Array and Hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {} #val:index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return c

# s = Solution
# nums = [2,7,11,15]
# target = 9
# result = sol.twoSum(nums, target)
# print(result)

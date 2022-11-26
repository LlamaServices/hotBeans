# [1,2,3,4], 3
# [0, 1]

class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
            hash = dict()
            for i in range(0, len(nums)):
                minus = target - nums[i]
                if minus in hash.keys():
                    return [i, hash.get(minus)]
                hash.update({nums[i]: i})
            return

print(Solution.twoSum([1,2,3,4], 3))
class Solution:
    def twoSum(self, nums, target):
        seen = {}  # number -> index
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []
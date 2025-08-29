class Solution:
    def twoSum(self, nums, target):
        seen = {}  # number -> index
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []



print(Solution().twoSum([2,7,11,15], 9))  # [0, 1]
print(Solution().twoSum([3,2,4], 6))      # [1, 2]
print(Solution().twoSum([3,3], 6))        # [0, 1]

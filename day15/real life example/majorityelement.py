class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate



#nums = [3, 2, 3]
sol = Solution()
#print(sol.majorityElement(nums))  # Output: 3

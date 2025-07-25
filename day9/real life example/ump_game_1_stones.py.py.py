class Solution:
    def canJump(self, nums):
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
        return True


#testing

 # Test Jump Game I
sol = Solution()
print(sol.canJump([2,3,1,1,4]))  # Output: True
print(sol.canJump([3,2,1,0,4]))  # Output: False
class Solution:
    def jump(self, nums):
        jumps = 0
        curr_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest
                
        return jumps


# Test Jump Game II
print(sol.jump([2,3,1,1,4]))     # Output: 2
print(sol.jump([2,1]))           # Output: 1
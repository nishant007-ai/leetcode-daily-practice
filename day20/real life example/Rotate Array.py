class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        nums.reverse()
   
        nums[:k] = reversed(nums[:k])

        nums[k:] = reversed(nums[k:])


#sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
#sol.rotate(nums, k)
print(nums)  # Output: [5,6,7,1,2,3,4]

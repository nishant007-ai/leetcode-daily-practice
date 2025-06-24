
238. Product of Array Except Self



class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n 


        

        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right  
            right *= nums[i]

        return res


input = 1,2,3,4
output = [24,12,8,6]


all done due to the res except

1 rec 1 
2 res 1*2
3 res 1*2*3
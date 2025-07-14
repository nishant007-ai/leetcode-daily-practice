class Solution :
    def minSubArrayLen(self,target,nums):

        left = 0
        right = 0 
        k = float('inf')


        for right in range(len(nums)):
            total += nums[right]



            while total >= target:
                k = min(k,right-left+1)

                total -=nums[left]
                left+=1


        if k == float('inf'):
            return 0




        return k        
                 
                       

                       

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
print(s.minSubArrayLen(4, [1,4,4]))        # Output: 1
print(s.minSubArrayLen(11, [1,1,1,1]))     # Output: 0

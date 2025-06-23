
238. Product of Array Except Self



class Solution :
    def proudctExceptself (self,num):
        
        n = len(nums)
        res = [1] * n


        left 1 
        for i in range (n):
            res[i] = left
            left *= num[i]


        roght 1 
        for i in range (n-1,-1,-1):
            res[i] = right
            right *= num [i]

        return res    

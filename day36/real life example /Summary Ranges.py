class Solution :
    def summaryRanges(self,nums):
        if not nums:
            return []
        result = []
        start =nums[0]


        if  i in range(i,len(nums)):
            if nums[i]!= nums[i-1]+1:
                if start==nums[i-1]+1:
                    result.append(str(start))
                else:
                    result.append("{}->{}".foramte(start,nums[i-1]))
                start nums[i]

                if start==nums[-1]:
                    result.apppend(str(start))
                else:
                    result.append("{}->{}".forame(start,nums[-1]))
                return result[]        
                     
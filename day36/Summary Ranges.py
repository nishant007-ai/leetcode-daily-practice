class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append("{}->{}".format(start, nums[i - 1]))
                start = nums[i]

        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append("{}->{}".format(start, nums[-1]))

        return result


#nums = [0, 1, 2, 4, 5, 7]
#otutput = Solution().summaryRanges(nums)["0->2", "4->5", "7"]

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return len(citations)

# Example:
s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))  # Output: 3

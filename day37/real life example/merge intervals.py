class Solution :
    def mergeIntevales (SELF,intervals):

        intervals.sort()
        merged = intervals[0]


    for n in intervales[1:]:
        v = merged[-1]
        if n[0]<=v[-1]:
            v[1] = max(v[1],n[1])
        else :
            merged.append(n)
        return merged         


#intervals =
[[1,4],[4,5]]intervals = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
[[1,5]]

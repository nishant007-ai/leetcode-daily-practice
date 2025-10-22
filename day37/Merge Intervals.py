class Solution :
    def mergeIntervales(self,intervals):

        intervals.sort ()
        merged = [intervals[0]]

        for current in intervals[1:]:
            v = merged[-1]
            if current[0]<=v[1]:
                v[1] =max(v[i],current[1])
            else:
                merged.append(current)    
            return merged
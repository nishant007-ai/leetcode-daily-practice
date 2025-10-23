class Solution :
    def insertInterval(self,n,k):
        result = []
        i = 0
        while i < len(n) and n[i][1] < k[0]:
            result.append(n[i])
            i +=1

        while i < len(n) and n[i][0] <= k[1]:
            k[0] = min(k[0],n[i][0])
            k[1] = max(k[1],n[i][1])
            i+=1
            result.append(k)

        while i < len(n):
            result.append(n[i])
            i+=1
        return result             
class Solution :
    def rotate(self,m):
        n = len(m)

        for i in range (n):
            for j in range(i+1,n):
                m[i][j],m[j][i]=m[j][i],m[i][j]


        for row in m:
            row.reverse()     

                
                
#A D G    →    G D A
#B E H    →    H E B
#C F I    →    I F C

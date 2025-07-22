class Solution :
    def spiralMatrix(self,m):
        result = []
        if m==0:
            return result
        

        top,bottom = 0,0. , len(m,)-1
        right,left = 0,0.  , len(m[0])-1



        while top <= bottom and left<=right:
            for i in range(left,right+1):
                result.append(m[top][i])
            top+=1


            for i in range(top,bottom+1):
                result.append(m[i][right])
            right-=1        


            for i in range (left,right-1,-1):
                result.append(m[bottom][i])
            bottom-=1



            for i in range(top,bottom-1,-1) :
                result.append(m[i][left])
            left+=1
        return result           


                

    

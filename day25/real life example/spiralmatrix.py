class Solution :
    def spiralMatrix(self,m):
        result= []

        if not m:
            return result
        
        top,bottom = 0,len(m)-1
        left,right= 0, len(m[0]-1)


        while top<=bottom and left<=right:
            for i in range(left,right+1):
                result.append(m[top][i])
            top+=1


            for i in range(top,bottom+1):
                result.append(m[i][right])
            right -=1 


            for i in range (left,right-1,-1) :
                result.append(m[bottom][i])
            bottom -=1

            for i in range (top,bottom-1,-1):
                result.append(m[i][left])
            left+=1

        return result

    #input=Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # #output=Output: [1,2,3,6,9,8,7,4,5]            
                  


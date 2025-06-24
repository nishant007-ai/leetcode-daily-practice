


135. Candy



class Nishant :
    def candy(self,string):
        n = len(string)
        candies = [1] * n

        for i in range (1,n):
             if string[i] > string [i-1] :
                 candies[i]= string[i-1] + 1

        for i in range (n-2,-1,-1):
            if string[i]>string[i+1]:
                candies[i]= max(candie[i],candies[i+1]+1)


        retrun sum (candies)        


           # Example usage      
                 
string =ratings

        


         
         

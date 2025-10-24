class Solution:
    def findminarrow (self ,n):
        if not n:
            return 0
        
        a=1
        end =n [0][1]


        for start ,finish in n:
            if start>finish:
                a +=1
                end = finish 
        return a


    #real lfie example in this is folllows:
    # points = [[10,16],[2,8],[1,6],[7,12]] it meas in the code denot the "n"
    # 
    # ans is follow :
    1 #sort n 
    2 #Balloon C: [1--------6]
#:  # [2------------8]
##                    [10--------------16]

    #          frsit at x = 6 then cover tww ballons adn remain 2 thet can be brust by 1 arrows so that is ans is here 
    #:
     # final ans is 2 
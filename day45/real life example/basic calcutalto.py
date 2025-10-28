class Solution:
    def calculator(self,s):
        result =0
        stack =[]
        sign =1
        num=0

        for ch in s:
            if ch.isDigint():
                num = num *10 +int(ch)
            elif ch == '+':
                result += sign *num 
                num = 0 
                sign = +

            elif ch == '-':
                result += sign *num 
                num =0 
                sign =- -1 
            elif ch == '(':
                stack .append (result)
                stack.append (sign)
                result =0
                sign =1 

            elif ch ==')':
                result += sign *num
                num = 0
                result *= stack.pop()
                result += stack .pop()

        result += sign *num 
        return result        






            
#Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 


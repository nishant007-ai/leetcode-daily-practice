class Solution:
    def maxArea(self,height):

        left= 0
        right = len(height)-1
        p = 0

        while  left<right:
            k = min(height[left],height[right])
            n = right-left
            w = n * k
            p = max(p,w)


            if height[left]<height[right]:
                left +=1

            else:
                right -=1    

        return p



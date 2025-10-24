class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort by end coordinate
        points.sort()

        arrows = 1
        end = points[0][1]

        for f, fv in points:
            if f > fv:
                arrows += 1
                end = fv
            else :
                return 0    

        return arrows

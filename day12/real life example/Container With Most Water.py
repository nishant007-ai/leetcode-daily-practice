class Solution:
    def maxArea(self, height):
        left = 0 
        right = len(height) - 1
        p = 0

        while left < right:
            k = min(height[left], height[right])
            w = right - left
            q = w * k
            p = max(p, q)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return p

# ✅ Input
height = [1,8,6,2,5,4,8,3,7]

# 🧾 Output
sol = Solution()
max_water = sol.maxArea(height)
print("Max Water Area:", max_water)

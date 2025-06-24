height = [3, 0, 2, 0, 4]


class Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0

        left = [0] * n
        right = [0] * n

        # Fill left[]
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        # Fill right[]
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        # Calculate water
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water



3 (at 1) + 1 (at 2) + 3 (at 3) = ✅ 7 units

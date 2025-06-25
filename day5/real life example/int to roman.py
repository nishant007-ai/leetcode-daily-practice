





















class Solution:
    def intToRoman(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        roman = ""
        i = 0
        
        while num > 0:
            count = num // val[i]
            roman += syms[i] * count
            num -= val[i] * count
            i += 1
        
        return roman


# Example test
sol = Solution()
print(sol.intToRoman(3749))  # Output: "MMMDCCXLIX"

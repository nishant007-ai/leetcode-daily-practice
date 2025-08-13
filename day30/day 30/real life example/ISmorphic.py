class Solution:
    def isIsomophic(self,s,t):
        if len(s) != len(t):
            return False
        
        mapping_s_to_t={}
        mapping_t_to_s={}
        
        for char_s, char_t in zip(s, t):
            if char_s not in mapping_s_to_t:
                mapping_s_to_t[char_s] = char_t
            if char_t not in mapping_t_to_s:
                mapping_t_to_s[char_t] = char_s
            
            if mapping_s_to_t[char_s] != char_t or mapping_t_to_s[char_t] != char_s:
                return False
        
        return True
    
    #Input: s = "egg", t = "add"

#Output: true
# Real-life example of Isomorphic Strings

# Imagine two people use different symbols for the same things.
# Person A: 🍎 for Apple, 🚗 for Car
# Person B: 🟥 for Apple, 🟦 for Car
# As long as each symbol maps to exactly one meaning and is consistent,
# their communication is "isomorphic".

# Example:
person_a = "🍎🚗🚗"
person_b = "🟥🟦🟦"
#print(are_isomorphic(person_a, person_b))  # Output: True


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]

            while word.find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix

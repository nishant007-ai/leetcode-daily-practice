class Solution:

    def     groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for s in strs:
            key = tpuple(sorted(s)
                         anagrams[key].append(s))
        return list(anagrams.values())
            key = tuple(sorted(s)) 
            anagrams[key].append(s)

        return list(anagrams.values())          
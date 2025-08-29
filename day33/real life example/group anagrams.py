class SOlution :
    def groupAnagrams(self,strs):

        key = defaultdict(list)

        for s in strs:
            key = touple (sorted(s))
            anagrams[key].append(s)

            return list(anagrams.valus())


#Input: strs = ["eat","tea","tan","ate","nat","bat"]

#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
class Solution:
    def groupAnagrams(self, strs):
        setHash = defaultdict(list)
        for i in strs:
            setHash[tuple(sorted(i))].append(i)
        return list(setHash.values())

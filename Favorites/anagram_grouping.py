# Given an array of words return the list grouped by anagrams.

import collections

def groupAnagramWords(strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups["".join(sorted(s))].append(s)
    return list(groups.values())

print(groupAnagramWords(['abc','cba','fep','pef','fer']))
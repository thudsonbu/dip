# Given a non-empty list of words, return the k most frequent words. The output should be
# sorted from highest to lowest frequency, and if two words have the same frequency,
# the word with lower alphabetical order comes first. Input will contain only lower-case letters.

from collections import Counter

class Solution(object):
  def topKFrequent(self, words, k):
    counter = Counter(words)
    freqs = {}
    for word, count in counter.items():
      if count not in freqs:
        freqs[count] = []
      freqs[count].append(word)
    res = []
    for i in range(len(words), 0, -1):
      if i in freqs:
        for word in freqs[i]:
          res.append((word, i))
      if len(res) >= k:
        break
    res = sorted(res, reverse=True, key=lambda x: x[1])
    return [element[0] for element in res]

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
        


            
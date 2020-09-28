# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given a list of words, for each word find the shortest unique prefix. You can assume a word will not be a substring of another word (ie play and playing won't be in the same words list)

# Example
# Input: ['joma', 'john', 'jack', 'techlead']
# Output: ['jom', 'joh', 'ja', 't']
# Here's some starter code:

# 1:21
class Node:
  def __init__(self):
    self.count = 0
    self.children = {}

class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, word):
    curr_node = self.root
    for c in word:
      if c not in curr_node.children:
        curr_node.children[c] = Node()
      curr_node = curr_node.children[c]
      curr_node.count += 1

  def unique_prefix(self, word):
    curr_node = self.root
    prefix = ''

    for c in word:
      if curr_node.count == 1:
        return prefix
      else:
        curr_node = curr_node.children[c]
        prefix += c
    return prefix

def shortest_unique_prefix(words):
  trie = Trie()

  for word in words:
    trie.insert(word)

  unique_pref = []
  for word in words:
    unique_pref.append(trie.unique_prefix(word))

  return unique_pref

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']


    

                
        


print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead'],1))
# ['jom', 'joh', 'ja', 't']

# def shortest_unique_prefix(words,length):
#     prefix_dict = {}
#     bad_keys = []
#     good_keys = []
#     for word in words:
#         new_prefix = word[0:length]
#         found_words = prefix_dict.get(new_prefix, None)
#         if found_words:
#             print(found_words)
#             prefix_dict[new_prefix] = [word] + prefix_dict[new_prefix]
#             if len(found_words) == 1:
#                 bad_keys += new_prefix
#                 good_keys.remove(new_prefix)
#         else:
#             prefix_dict[new_prefix] = [word]
#             good_keys += new_prefix

#     bad_words = []
#     if len(bad_keys) > 0:
#         for key in bad_keys:
#             bad_words += prefix_dict[key]
#         good_keys += shortest_unique_prefix(bad_words,length+1)

#     return set(good_keys)
# Implement auto-completion. Given a large set of words (for instance 1,000,000 words) and 
# then a single word prefix, find all words that it can complete to.

class Node:
    def __init__(self, isWord, children):
        self.isWord = isWord # if this is the end of a word we need to know
        self.children = children

class Solution:
    def build(self, words):
        trie = Node(False, {})
        # traverse tree adding new children if not there
        for word in words:
            current = trie
            for char in word:
                if not char in current.children:
                    current.children[char] = Node(False, {})
                current = current.children[char]
            current.isWord = True
        self.trie = trie
    
    def autocomplete(self, word):
        current = self.trie
        for char in word:
            if not char in current.children:
                return []
            current = current.children[char]

        words = []
        self.dfs(current, word, words)
        return words

    def dfs(self, node, prefix, words):
        if node.isWord:
            words.append(prefix)
        for char in node.children:
            self.dfs(node.children[char], prefix + char, words)

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']
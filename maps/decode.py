# You are given the strings key and message, which represent a cipher key and a
# secret message, respectively. The steps to decode message are as follows:

# Use the first appearance of all 26 lowercase English letters in key as the
# order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one
# instance of each letter in the alphabet), we have the partial substitution
# table of
# ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

# Return the decoded message.


class Solution:
    def decodeMessage(self, key, message):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        alphaset = set(alphabet)
        alphamap = dict()

        idx = 0
        for char in key:
            if char in alphaset and char not in alphamap:
                alphamap[char] = alphabet[idx]
                idx += 1

            if idx > 25:
                break

        decoded = ""
        for char in message:
            if char in alphaset:
                decoded = decoded + alphamap[char]
            else:
                decoded = decoded + char

        return decoded

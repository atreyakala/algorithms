# babc
# {
#     "c": {"*": True},
#     "b": {
#         "c": {"*": True},
#         "a": {
#             "b": {
#                 "c": {"*": True}
#             }
#         }
#     },
#     "a": {
#         "b": {
#             "c": {"*": True}
#         }
#     }
# }

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubStringStartingAt(i, string)

    def insertSubStringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            char = string[j]
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[char]
        return self.endSymbol in node

trie = SuffixTrie("babc")
trie.contains("abc")

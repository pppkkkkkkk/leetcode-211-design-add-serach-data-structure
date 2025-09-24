class TrieNode:
    def __init__(self):
        self.child = {}
        self.endWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.endWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, index) -> bool:
            if index == len(word):
                return node.endWord

            if word[index] == '.':
                for kid in node.child.values():
                    if dfs(kid, index+1):
                        return True

            if word[index] in node.child:
                return dfs(node.child[word[index]], index+1)            

            return False
        return dfs(curr, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
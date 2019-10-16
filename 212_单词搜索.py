class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        new_list = []
        new_str = ''
        for i in range(len(board)):
            for num in board[i]:
                new_list.append(num)
        for i in range(len(new_list)):
            new_str += new_list[i]
        
        trie = Trie()
        res = []
        for i in new_str:
            print(i)
            trie.insert(i)

        for i in range(len(words)):
            if trie.search(words[i]):
                res.append(words[i])
        
        return res
            
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False # 空心还是实心

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.word = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        if cur.word:
            return True
        else:
            return False


sol = Solution()
words = ["oath","pea","eat","rain"]
board =[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
print(sol.findWords(board, words))

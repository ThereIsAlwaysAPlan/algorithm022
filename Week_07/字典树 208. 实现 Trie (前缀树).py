#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2021-01-26 22:31:21
# @Author: xiaochuan
# @Description: 208. 实现 Trie (前缀树)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_words = '#'  # 记录词的结束符

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_words] = self.end_of_words

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_words in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

if __name__ == "__main__":
    # Your Trie object will be instantiated and called as such:
    word = 'abc'
    prefix = 'b'
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)
    print(obj.root,param_2,param_3)

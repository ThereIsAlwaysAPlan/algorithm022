from typing import List
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 双向BFS 哪个长度小，遍历哪个，遇到一个在对面集合了，那就找到了
        if endWord not in wordList:
            return 0
        # 预处理
        front = {beginWord}
        back = {endWord}
        wordList = set(wordList)
        dist = 1

        while front and back:
            dist += 1
            nxt_front = set()
            for word in front: # loop front
                for i in range(len(word)): # loop every char in the word
                    for c in string.ascii_lowercase: # from 'a'-'z' replace one char
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in back: # judge 是否相交
                                return dist
                                
                            if new_word in wordList: # 将所有的改变一个字符得到的word写入下一个循环中
                                nxt_front.add(new_word)
                                wordList.remove(new_word)
            front = nxt_front
            if len(front)>len(back):
                front,back = back,front
        return 0

        # 单向BFS 
        # if endWord not in wordList:
        #     return 0
        # start = {beginWord}
        # wordList = set(wordList)
        # dist = 1
        # while start:
        #     dist += 1
        #     nxt = set()
            
        #     for word in start:
        #         for i in range(len(word)):
        #             for c in [chr(i) for i in range(97,123)]:
        #                 if c != word[i]:
        #                     new_word = word[:i] + c + word[i+1:]
        #                     if new_word == endWord:
        #                         return dist
                            
        #                     if new_word in wordList:
        #                         nxt.add(new_word)
        #                         wordList.remove(new_word)
        #     start = nxt
        # return 0
                        
        # DFS 改变一个字符，改变后的word如果在wordList中，那就遍历下一层，递归结束条件，word=endWord
                # DFS 改变一个字符，改变后的word如果在wordList中，那就遍历下一层，递归结束条件，word=endWord
        if endWord not in wordList:
            return 0
        
        mi = float('inf') # 保存最短路径
        wordList = set(wordList)
        def dfs(level,word):
            nonlocal mi
            # terminator
            if word == endWord:
                if level < mi:
                    mi = level + 1
                return 
            
            # process
            # 剪枝 : 递归深度超过当前最短路径，说明当前路径肯定不是最短的，返回
            if level > mi:
                return 
            for i in range(len(word)):
                for c in [chr(i) for i in range(97,123)]:
                    if word[i] != c:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordList:
                            # drill down
                            wordList.remove(new_word)
                            dfs(level+1,new_word)
                            # revert
                            wordList.add(new_word)
        dfs(0,beginWord)
        return mi if mi != float('inf') else 0


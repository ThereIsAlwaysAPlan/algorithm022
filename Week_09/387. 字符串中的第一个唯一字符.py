# -*- coding: UTF-8 -*-

# @Created on 2021/02/21 22:35:31 周日
# @387. 字符串中的第一个唯一字符.py
# @author: xiaochuan
# @description: leetcode


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 1.暴力
        # find = set()
        # for i in range(len(s)):
        #     if s[i] in find:
        #         continue
        #     else:
        #         find.add(s[i])
        #         for j in range(i+1,len(s)):
        #             if s[i] == s[j] :
        #                 break
        #         else:
        #             return i
        # return -1

        # 2.hash
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1

if __name__ == "__main__":
    print(Solution().firstUniqChar('loveleetcode'))
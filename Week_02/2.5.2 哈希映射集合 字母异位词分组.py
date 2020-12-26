#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2020-12-26 16:48:10
# @Author: xiaochuan
# @Description: 字母异位词分组

# 思路：字符串元素排序，将其转变为不可变的元组之后，作为字典的键，原本值作为键对应的值存入字典中
class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return [i for i in dict.values()]
    
if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
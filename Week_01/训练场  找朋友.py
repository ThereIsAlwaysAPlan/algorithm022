#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2020-12-22 20:58:51
# @Author: xiaochuan
# @Description: 找朋友

class Solution:
    # 找朋友
    def findMinMinutes(self, n, k):
        if n >= k :
            return k -n
        else:
            # time1 = int(math.log2(k/n)) # 计算时间，向上取整
            # new_n = n * math.pow(time1,2) # 计算新的N，仍<K
            # return time1 + (k - new_n > new_n*2-k ? new_n*2-k : k-new_n)
            s = set()  # 存放已访问的节点
            s.add(n)  # 初始化
            d = {}  # 存放每分钟到达节点
            d[0] = {n}
            i = 0
            while True:
                tmp = set()
                # 遍历当前分钟能到达的节点
                for x in d[i]:       
                    if x - 1 == k or x+1 == k or 2*x ==k :
                        return i + 1
                    else:
                        # skip 已访问过的节点
                        if x - 1 >= 0 and x - 1 not in s:
                            tmp.add(x-1)
                            s.add(x-1)
                        if x+1 not in s:
                            tmp.add(x+1)
                            s.add(x+1)
                        if 2*x not in s:
                            tmp.add(2*x)
                            s.add(2*x)
                i += 1
                d[i] = tmp
                        
            return -1

if __name__ == "__main__":
    print(Solution().findMinMinutes(3,32))
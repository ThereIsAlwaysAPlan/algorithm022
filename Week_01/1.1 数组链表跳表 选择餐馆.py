#!/usr/bin/env python
# -*- coding:utf-8 -*-


# @CreationDate: 2020-12-14 10:51:57
# @Author: xiaochuan
# @Description: 选择餐馆

# 测试用例
restaurants = [[0,4,1,40,10],[1,8,0,50,5],[2,8,1,30,4],[3,10,0,10,3],[4,8,1,15,1]]
filters = [0, 40, 10]
class Solution:
    def filterRestaurants(self, restaurants, filters):
        # results = []
        # # 筛选符合条件的餐馆
        # results = self.choose_restruants(restaurants,filters)
        # # 排序
        # return self.sort_restaurant(results)
        return self.sort_restaurant(self.choose_restruants(restaurants,filters))

    def choose_restruants(self,restaurants,filters):
        results = []
        for rest in restaurants:
            if filters[1] >= rest[3] and filters[2] >= rest[4]:
                if filters[0] == 1 and rest[2] == 1 or filters[0] == 0:
                    results.append(rest)
        return results

                
    def sort_restaurant(self,results):
        # id 从高到底 
        results.sort(key =lambda x: x[0],reverse=True)
        # ratings 从高到底
        results.sort(key =lambda x: x[1],reverse=True)
        return [i[0] for i in results]

if __name__ == "__main__":
    print(Solution().filterRestaurants(restaurants,filters))
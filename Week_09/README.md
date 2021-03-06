高级DP的复杂度来源：
1.其状态更多维（二维、三维...，涉及压缩）
2.状态转移方程更加复杂
本质：逻辑抽象化，数学思维，内功（多练多思考，扎实基础，知道了框架（公式），按照这个方向去思考问题，想想小学6年级怎么做题的）

不同路径2：
DP状态(压缩)：DP[j]表示到j为止的不同路径的方法数
DP方程：
    if road[i][j] == 1:
        dp[j] = 0
    elif j > 0:   # 这里没有包含的j为0的情况，是因为没必要，因为跟上一层值保持一致，即上面是通的，这里就是通的，上面若是有堵塞，那么本列下面所有的路都不能走
        dp[j] += dp[j-1]


爬楼梯 进阶：
1.1，2，3   
    DP方程：a(i) = a(i-1)+a(i-2)+a(i-3)
2.X1,X2,...,Xm （各元素均不相同，不然就没意思了）
    DP方程：loop j : 0->m-1  a(i) += a(i-x[j])
3.不能走跟上一层一样的步数【需要增加一个维度】
    状态：a[i][k] i:走到第i层（有多少种方式） k：走到第i层用的是多少步
    DP方程：loop i:0->n-1
                loop j:0->m-1
                    loop k:0->m-1
                        if j != k:
                            a[i][x[k]] += a[i-x[k]][x[j]]

高级字符串算法中，与DP相关的题目：
1.最长子序列（两个字符串比较）
DP状态：DP(i,j) 表示s1前i个字符和s2前j个字符的最长子序列长度
DP方程：
    if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1]+1
    else:
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])

2.最长公共子串（两个字符串比较）
DP状态：DP(i,j) 表示s1前i个字符和s2前j个字符的最长公共子串长度
DP方程：
    if s1[i-1]==s2[j-1]:
        DP[i][j] = dp[i-1][j-1]+1
    else:
        dp[i][j] = 0
3.编辑距离（A串通过每次替换/插入/删除变成B串的最小次数）
方法1：two-end BFS
方法2：DP
    状态：dp(i,j) 表示w1[:i]和w2[:j]的最小编辑距离
    DP方程：
        if w1[i-1] == w2[j-1]:
            dp(i,j) = dp(i-1,j-1)
        else:
            dp(i,j) = min(dp(i-1,j-1) + 1,   # 经过一次替换后的最小编辑距离
                          dp(i-1,j) + 1,    # 经过一次删除（或增加），∵w1，w2长度总有一个长，一个短，变化的结果总是使两者长度向中间靠拢
                          dp(i,j-1) + 1)    # 经过一次增加（或删除）

字符串的正则表达式实现：
思路：DP
DP状态：DP(i,j) 双字符串问题均考虑二维实现
第一步：不考虑匹配符，来匹配两个字符串
第二步：第一步的递归实现（只匹配第一个字符，将剩余字符的匹配放入下层递归，分治思想）
第三步：考虑匹配符.
第四步：考虑匹配符*
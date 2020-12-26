学习笔记

hashtable的使用场景，如果一类问题是涉及到 分门别类 的，可以考虑使用。

因为哈希表的特性，首先键是不可变的，所以适合用来存储共性（相似性）结构值，并将原始数据作为共性结构对应的字典的值；
其次，哈希表lookup的时间复杂度是O(1)，这就能将原本需要暴力或枚举的问题从O(n^2)的时间复杂度优化为O(n)


二叉树遍历相关：
前、中、后序遍历
常规遍历方式：
1.递归 time:O(n) space:O(n)
模板
前序遍历：
def pre_order(root):
    return [root.val] + pre_order(root.left) + pre_order(root.right)
中序遍历：
def in_order(root):
    return in_order(root.left) + [root.val] + in_order(root.right)
后序遍历：
def post_order(root):
    return post_order(root.left) + post_order(root.right) + [root.val]

2.迭代（以 颜色标记法 为主，因3种遍历格式可复用）time:O(n) space:O(n)
模板
# 重点：1.该方法将未访问的节点标记为WHITE,已访问节点标记为GRAY, 在遍历到Gray颜色时，就将当前节点记录到结果集中；
#      2.实际上也是模拟栈，根据栈 LIFO 的特性，如果要保证遍历结果为想要的结果，需根据前/中/后序遍历的特性，将节点逆序压入栈中  
#        例如：前序要求：根——左——右，即出栈结果为 根——左——右 ，那么压入栈的顺序应为：右——左——根
# 颜色标记法  模拟栈 
# 前序：出栈：根——左——右  入栈：右——左——根
# 中序：出栈：左——根——右  入栈：右——根——左
# 后续：出栈：左——右——根  入栈：根——左——右
# 优化：如果子节点为空，不需要入栈
WHITE,GRAY = 0,1
res = []
stack = [(WHITE,root)]
while stack:
    color,node = stack.pop()
    if not node: continue
    if color == WHITE:
        if node.right:
            stack.append((WHITE,node.right))
        stack.append((GRAY,node))
        if node.left:
            stack.append((WHITE,node.left))
    else:
        res.append(node.val)
return res

3.迭代，就是模拟栈
模板
N叉树前序遍历： 出栈：根——左——右  入栈：输出根节点，先压右，再压左
def pre_order(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        for i in node.children[::-1]:
            stack.append(i)
    return

二叉树中序遍历： 先遍历左子树，然后左儿子出栈（存入结果集），根出栈，压入右子树，循环
def in_order(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right
    return res
        
N叉树后序遍历：出栈：左——右——根  入栈：根——右——左 
def post_order(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        stack.extend(node.children)
    return res[::-1]

4.morris算法 time:O(n) space:O(1)

======================================================================================
N叉树层序遍历
1.BFS——deque time:O(n) space:O(n)
# 重点：使用len(queue)来记录当前层的元素个数，作为循环遍历的次数，循环结束，当前层就被全部访问一遍了
def level_order(root):
    if not root:
        return []
    res = []
    queue = collections.deque([root])
    while queue:
        res.append([])
        for _ in range(len(queue)):
            node = queue.popleft()
            res[-1].append(node.val)
            queue.extend(node.children)
    return res
        
2.BFS——双指针 time:O(n) space:O(n)
# 重点：prev记录父节点数据，curr记录所有子节点 loop prev -> res,prev.children -> curr
def level_order(root):
    if not root:
        return []
    res = []
    prev = root
    while prev:
        curr = []
        res.append([])
        for node in prev:
            res[-1].append(node.val)
            curr.extend(node.children)
        prev = curr
    return res

3.递归 time:O(n) space:O(logn) 最坏：O(n) 取决于堆栈的高度
# 重点： 每层递归的时候传入 当前层数
def level_order(root):
    if not root:
        return []
    res = []
    
    def order(root,level):
        # terminator condition
        if not root:
            return None
        # process curr information
        # res长度不够，进行扩展
        if len(res) == level:
            res.append([])
        # 添加根节点到当前层
        res[level].append(root.val)

        # extend child nodes
        for node in root.children:
            order(node,level+1)
    
    order(root,0)
    return res



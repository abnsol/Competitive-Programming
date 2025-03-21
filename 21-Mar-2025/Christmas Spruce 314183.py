# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict

n = int(input())

parent_child = defaultdict(int)
count_leaf = defaultdict(int)
leafs = set()

for i in range(2,n + 1):
    parent = int(input())

    if parent in leafs:
        count_leaf[parent_child[parent]] -= 1
        leafs.remove(parent)
    
    count_leaf[parent] += 1
    parent_child[i] = parent
    leafs.add(i)

flag = True
for key in count_leaf:
    if count_leaf[key] < 3:
        flag = False

print("Yes" if flag else "No")
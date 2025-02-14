# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n,k = map(int, input().split())
a = list(map(int, input().split()))

hashmap = defaultdict(int)
l = 0
ans_l, ans_r = -1, -2
for r in range(n):
    hashmap[a[r]] += 1
    while len(hashmap) > k:
        hashmap[a[l]] -= 1
        if hashmap[a[l]] == 0:
            del hashmap[a[l]]
        l += 1
    
    if ans_r - ans_l < r - l:
        ans_l, ans_r = l, r


print(ans_l + 1,ans_r + 1)
    
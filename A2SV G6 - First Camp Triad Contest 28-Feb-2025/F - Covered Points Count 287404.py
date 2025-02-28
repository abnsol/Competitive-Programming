# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import defaultdict

t = int(input())
mp = defaultdict(int)
for _ in range(t):
    l,r = map(int, input().split())
    mp[l] += 1
    mp[r + 1] -= 1

keys = sorted(mp.keys())
# print(mp)


n = len(keys)
ans = defaultdict(int)
ttl = 0
for i in range(n - 1):
    # print("ttl",ttl)
    ttl += mp[keys[i]]
    ans[ttl] += (keys[i + 1] - keys[i])

res = []
for i in range(1,t + 1):
    res.append(ans[i])

print(*res)


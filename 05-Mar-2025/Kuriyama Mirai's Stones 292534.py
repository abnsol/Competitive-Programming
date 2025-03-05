# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))
m = int(input())
queries = []
for _ in range(m): 
    queries.append(list(map(int, input().split())))

prefixA = list(accumulate([0] + a))
sorted_cost = list(accumulate([0] + sorted(a)))

for t,l,r in queries:
    if t == 1:
        print(prefixA[r] - prefixA[l - 1])
    else:
        print(sorted_cost[r] - sorted_cost[l - 1])
# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

from math import ceil
n,m,k = map(int,input().split())
print(ceil(n/k) * ceil(m/k))
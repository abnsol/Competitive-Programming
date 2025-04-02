# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
a = list(map(int, input().split()))

b = []
for i in range(1,n): b.append(a[i - 1] - a[i])
b.sort()
res = a[-1] - a[0]
for i in range(k - 1): res += b[i]
print(res)
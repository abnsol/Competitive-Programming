# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n,k = map(int, input().split())
a = list(map(int, input().split()))

window = ttl = 0
for i in range(k):
    window += a[i]

ttl += window
for i in range(k,n):
    window -= a[i - k]
    window += a[i]
    ttl += window

print(ttl/(n - k + 1))

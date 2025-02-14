# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t = map(int, input().split())
books = list(map(int, input().split()))
ans = l = 0
ttl = 0
 
for r in range(n):
    ttl += books[r]
    while ttl > t:
        ttl -= books[l]
        l += 1
    
    ans = max(ans,r - l + 1)
print(ans)
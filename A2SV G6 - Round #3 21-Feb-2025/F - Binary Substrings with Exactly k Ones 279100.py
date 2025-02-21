# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import Counter

n = int(input())
a = input()

dic = Counter({0:1})
ans = ttl = 0
for r in range(len(a)):
    ttl += int(a[r])
    ans += dic[ttl - n]
    dic[ttl] += 1
    
print(ans)
# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

n = int(input())
c = 'codeforces'
for i in range(n):
    ans = 0
    w = input()
    a = len(w)
    for i in range(a):
        if w[i] != c[i]:
            ans += 1
    print(ans)
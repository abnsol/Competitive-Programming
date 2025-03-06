# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    i = 1
    while i < n:
        if a[i] < a[i - 1]:
            ans += 1
            i += 2
        else:
            i += 1
    
    print(ans)
# Problem: Sum - https://codeforces.com/contest/1742/problem/A

n = int(input())
for i in range(n):
    a = sorted(map(int, input().split()))
    print("YES" if a[-1] == a[-2] + a[-3] else "NO")


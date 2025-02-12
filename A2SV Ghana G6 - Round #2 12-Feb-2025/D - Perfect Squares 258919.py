# Problem: D - Perfect Squares - https://codeforces.com/gym/586964/problem/D

import math
n = int(input())
a = sorted(map(int, input().split()))

for i in range(n - 1,-1,-1):
    if a[i] < 0:
        print(a[i])
        exit()

    sqr = math.floor(math.sqrt(a[i]))
    if sqr * sqr != a[i]:
        print(a[i])
        exit()
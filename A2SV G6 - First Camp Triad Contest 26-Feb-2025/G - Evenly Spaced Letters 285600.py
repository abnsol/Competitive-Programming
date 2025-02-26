# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

from collections import Counter

t = int(input())
for _ in range(t):
    a = input()
    n = len(a)
    cnt = Counter(a)
    arr = [0] * n

    idx = 0
    direction = 0

    for key in cnt:
        if cnt[key] == 2:
            arr[idx] = key
            arr[idx + 2] = key

            if direction % 2 == 0:
                idx += 1
                direction += 1
            else:
                idx += 3
                direction -= 1
        # del cnt[key]
    
    idx = 0
    for key in cnt:
        if cnt[key] == 1:
            while idx < n and arr[idx] != 0:
                idx += 1
            arr[idx] = key
    
    print("".join(arr))
    
    
    
    
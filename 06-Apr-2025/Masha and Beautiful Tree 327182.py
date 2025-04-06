# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())
for _ in range(t):
    m = int(input())
    perm = list(map(int,input().split()))
    _sorted = list(range(1,m + 1))

    if perm == _sorted:
        print(0)
        continue

    count = 0
    def mergesort(arr):
        global count
        if len(arr) <= 1:
            return arr
        
        mid = len(arr)//2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])

        if left[-1] > right[0]:
            count += 1
            return right + left
        return left + right
    
    if mergesort(perm) == _sorted:
        print(count)
    else:
        print(-1)
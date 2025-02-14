# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input())))
    
    mat1 = [list(row) for row in zip(*mat[::-1])]
    mat2 = [list(row) for row in zip(*mat1[::-1])]
    mat3 = [list(row) for row in zip(*mat2[::-1])] 
                
    # print(mat1)
    # print(mat2)
    # print(mat3)

    ans = 0
    for r in range(n//2):
        for c in range(r,n - 1 - r):
            cnt = Counter([mat[r][c],mat1[r][c],mat2[r][c],mat3[r][c]])
            if cnt[0] > cnt[1]:
                ans += cnt[1]
            else:
                ans += cnt[0]
    
    print(ans)

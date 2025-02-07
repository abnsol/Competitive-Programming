# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def inbound(i,n,j,m):
    return 0 <= i < n and 0 <= j < m

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
# n,m = 4,4
# mat = [[1 ,2, 2, 1],[2,4,2,4],[2,2,3,1],[2,4,2,4]]
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))

    construct = [[-1,-1],[-1,1]]
    dirs = [[1,-1],[1,1]]

    newMat = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            idx = 0
            val = [mat[i][j],mat[i][j]]  
            for r,c in construct:
                nr, nc = i + r, j + c
                if inbound(nr,n,nc,m):
                    if not idx:
                        val[0] += newMat[nr][nc][0]
                    else:
                        val[1] += newMat[nr][nc][1]
                idx += 1
            newMat[i][j] = val

    ans = 0
    for i in range(n):
        for j in range(m):
            ttl = idx = 0
            for r,c in dirs:
                nr ,nc = i,j
                while inbound(nr + r,n,nc + c,m):
                    nr += r
                    nc += c
                if not idx:
                    ttl += newMat[nr][nc][1]
                else:
                    ttl += newMat[nr][nc][0]
                idx += 1
            ttl -= mat[i][j]
            ans = max(ans,ttl)
    print(ans)

                
# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

def solve():
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append([a, b, i+1])
        
    arr.sort()
    
    ans = -1
    for i in range(1, n):
        if arr[i][1] <= arr[i-1][1]:
            ans = arr[i][2]
            break
        
        elif arr[i][0] <= arr[i-1][0] and arr[i][1] >= arr[i-1][1]:
            ans = arr[i-1][2]
            break
        
        arr[i][0] = max(arr[i][0], arr[i-1][1] + 1)
        
    print(ans)
 
 
solve()

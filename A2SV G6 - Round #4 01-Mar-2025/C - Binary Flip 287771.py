# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

import sys

def solve():
    n = int(input())
    A = input()
    B = input()
    
    A += '0'
    B += '0'
    count = 0
    
    for i in range(n):
        # If count == 0, it means we have equal 1s and 0s
        if A[i] == '1':
            count += 1
        else:
            count -= 1
        
        if count != 0:
            if A[i] != B[i] and A[i+1] == B[i+1]:
                print("NO")
                return
            
            elif A[i] == B[i] and A[i+1] != B[i+1]:
                print("NO")
                return
        
        # Alternative way of writing the above condition
        # if ((A[i] == B[i]) != (A[i + 1] == B[i + 1])) and count != 0:
        #     print("NO")
        #     return
    
    print("YES")


t = int(input())
for _ in range(t):
    solve()
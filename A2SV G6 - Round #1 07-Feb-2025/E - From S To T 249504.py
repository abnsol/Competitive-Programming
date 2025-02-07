# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter
n = int(input())

def helper(s,t,p):
    dicp = Counter(p)
    i = j = 0
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i += 1
            j += 1
        else:
            if i < len(s) and s[i] not in t:
                return "NO"
            elif t[j] in dicp and dicp[t[j]] > 0:
                dicp[t[j]] -= 1
                j += 1
            else:
                return "NO"
    if i < len(s):
        return "NO"
    
    return "YES"

            
for _ in range(n):
    s = input()
    t = input()
    p = input()
    print(helper(s,t,p))

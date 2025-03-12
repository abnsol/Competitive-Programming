# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input()))

    zero_stk = [] 
    one_stk = []
    ans = [0] * (n)
    sub = 0
    for idx,num in enumerate(a):
        if num == 0:
            if one_stk:
                cur_sub = one_stk.pop()
            else:
                sub += 1
                cur_sub = sub
            zero_stk.append(cur_sub)
        else:
            if zero_stk:
                cur_sub = zero_stk.pop()
            else:
                sub += 1
                cur_sub = sub
            one_stk.append(cur_sub)
        ans[idx] = cur_sub


    print(sub) 
    print(*ans)






    



    # print(cnt)   
    # print(*ans)


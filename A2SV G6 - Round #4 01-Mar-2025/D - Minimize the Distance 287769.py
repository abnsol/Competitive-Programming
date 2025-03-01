# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
points = [int(i) for i in input().split()]
points.sort()

mid_index = (n - 1) // 2
print(points[mid_index])
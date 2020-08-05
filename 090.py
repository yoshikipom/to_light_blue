# https://atcoder.jp/contests/s8pc-5/tasks/s8pc_5_b


def distance(p1, p2):
    dxx = (p1[0] - p2[0]) ** 2
    dyy = (p1[1] - p2[1]) ** 2
    return (dxx + dyy)**(1/2)


n, m = list(map(int, input().split()))

P = [list(map(int, input().split())) for i in range(n)]
Q = [list(map(int, input().split())) for i in range(m)]

if P:
    result = min(list(map(lambda x: x[2], P)))
else:
    result = float('inf')
for i in range(m):
    p1 = Q[i]
    for j in range(i+1, m):
        p2 = Q[j]
        result = min(result, distance(p1, p2)/2)
    for j in range(n):
        p2 = P[j]
        result = min(result, distance(p1, p2) - p2[2])

print(result)

# https://atcoder.jp/contests/abc074/tasks/arc083_b

import copy

N = int(input())
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

A2 = copy.deepcopy(A)
for k in range(N):
    for i in range(N):
        for j in range(N):
            A2[i][j] = min(A2[i][j], A2[i][k] + A2[k][j])

for i in range(N):
    for j in range(N):
        if A[i][j] != A2[i][j]:
            print(-1)
            exit()

result = 0
for i in range(N):
    for j in range(N):
        flag = True
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            if A2[i][j] == A[i][k]+A[k][j]:
                flag = False
                break
        if flag:
            result += A[i][j]

print(result//2)

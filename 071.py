# https://atcoder.jp/contests/s8pc-1/tasks/s8pc_1_e
from itertools import accumulate

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
C = list(map(int, input().split()))
for i in range(Q):
    C[i] -= 1

B = []
for i in range(1, N):
    B.append(pow(A[i-1], A[i], 10 ** 9 + 7))

D = [0] + list(accumulate(B))
# print(D)

result = 0
now = 0
for c in C:
    result = (result + abs(D[c] - D[now])) % (10 ** 9 + 7)
    now = c
    # print(c, result)
result = (result + D[now]) % (10 ** 9 + 7)

print(result)

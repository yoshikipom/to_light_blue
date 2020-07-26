# https://atcoder.jp/contests/abc014/tasks/abc014_3
n = int(input())
Q = [list(map(int, input().split())) for _ in range(n)]

A = [0 for _ in range(10 ** 6 + 2)]

for q in Q:
    a, b = q
    A[a] += 1
    A[b+1] -= 1

B = [0 for _ in range(10 ** 6 + 2)]
tmp = 0
for i in range(10 ** 6 + 2):
    tmp += A[i]
    B[i] = tmp

print(max(B))

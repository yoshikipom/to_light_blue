# https://atcoder.jp/contests/joi2017yo/tasks/joi2017yo_d

INF = 100000

N, M = list(map(int, input().split()))
A = [[0 for _ in range(N)] for _ in range(M)]
C = {}
for i in range(M):
    C[i] = 0
for i in range(N):
    number = int(input()) - 1
    A[number][i] = 1
    C[number] += 1

B = []
for i in range(M):
    cnt = 0
    row = []
    for j in range(N):
        row.append(cnt)
        cnt += A[i][j]
    row.append(cnt)
    B.append(row)

dp = [INF for i in range(1 << M)]
dp[0] = 0

for bit in range((1 << M) - 1):

    next_list = []
    left = 0
    for i in range(M):
        if (bit >> i) & 1:
            left += C[i]
        else:
            next_list.append(i)

    for i in next_list:
        right = left + C[i]

        cost = C[i] - (B[i][right] - B[i][left])
        next_bit = bit | (1 << i)

        if dp[next_bit] > dp[bit] + cost:
            dp[next_bit] = dp[bit] + cost

print(dp[-1])

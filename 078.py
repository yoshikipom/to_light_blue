# https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho1
# MLE
m, n = list(map(int, input().split()))
k = int(input())
M = [input() for _ in range(m)]
Q = [list(map(int, input().split())) for _ in range(k)]

J = [[0 for _ in range(n+1)] for _ in range(m+1)]
O = [[0 for _ in range(n+1)] for _ in range(m+1)]
I = [[0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m + 1):
    for j in range(1, n+1):
        J[i][j] += J[i][j-1]
        O[i][j] += O[i][j-1]
        I[i][j] += I[i][j-1]
        if M[i-1][j-1] == 'J':
            J[i][j] += 1
        elif M[i-1][j-1] == 'O':
            O[i][j] += 1
        elif M[i-1][j-1] == 'I':
            I[i][j] += 1

for i in range(1, m + 1):
    for j in range(1, n+1):
        J[i][j] += J[i-1][j]
        O[i][j] += O[i-1][j]
        I[i][j] += I[i-1][j]

# for row in J:
    # print(*row)
# print(*O)
# print(*I)

for q in Q:
    a, b, c, d = q
    result_j = J[c][d] - J[a-1][d] - J[c][b-1] + J[a-1][b-1]
    result_o = O[c][d] - O[a-1][d] - O[c][b-1] + O[a-1][b-1]
    result_i = I[c][d] - I[a-1][d] - I[c][b-1] + I[a-1][b-1]
    print(result_j, result_o, result_i)

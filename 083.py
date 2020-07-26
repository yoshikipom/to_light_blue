# https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_a
n, m = list(map(int, input().split()))
P = list(map(int, input().split()))
for i in range(m):
    P[i] -= 1
ABC = [list(map(int, input().split())) for _ in range(n-1)]

X = [0 for _ in range(n)]
cur = P[0]
for p in P[1:]:
    a = cur
    b = p
    if b < a:
        a, b = b, a
    X[a] += 1
    X[b] -= 1
    cur = p

Y = [0 for _ in range(n)]
Y[0] = X[0]
for i in range(1, n):
    Y[i] = Y[i-1] + X[i]
    # print(Y)

# print(*X)
# print(*Y)

result = 0
for i in range(n-1):
    a, b, c = ABC[i]
    ticket = a * Y[i]
    ic = b * Y[i] + c
    result += min(ticket, ic)
    # print(result)

print(result)

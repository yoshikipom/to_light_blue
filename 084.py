# https://atcoder.jp/contests/joi2012ho/tasks/joi2012ho4
n, m = map(int, input().split())
s = [[0 for j in range(n+2)] for i in range(n+2)]
for _ in range(m):
    a, b, x = list(map(int, input().split()))
    a -= 1
    b -= 1
    x += 1
    s[a][b] += 1
    s[a][b+1] -= 1
    s[a+x][b] -= 1
    s[a+x+1][b+1] += 1
    s[a+x][b+x+1] += 1
    s[a+x+1][b+x+1] -= 1

# 右
for i in range(1, n):
    for j in range(1, i+1):
        s[i][j] += s[i][j-1]

# 下
for i in range(1, n):
    for j in range(i):
        s[i][j] += s[i-1][j]

# 右下
for i in range(1, n):
    for j in range(1, i+1):
        s[i][j] += s[i-1][j-1]

ans = 0
for i in range(n):
    for j in range(i+1):
        if s[i][j]:
            ans += 1
print(ans)

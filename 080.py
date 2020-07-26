# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_d
h, w, k, v = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(h)]

B = [[0 for _ in range(w+1)] for _ in range(h+1)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        B[i][j] += B[i][j-1]
        B[i][j] += A[i-1][j-1]

for i in range(1, h + 1):
    for j in range(1, w+1):
        B[i][j] += B[i-1][j]

result = 0
for h1 in range(h):
    for w1 in range(w):
        for h2 in range(h1, h):
            for w2 in range(w1, w):
                area = (h2 - h1 + 1) * (w2-w1+1)
                house = area * k
                land = B[h2+1][w2+1] - B[h2+1][w1] - B[h1][w2+1] + B[h1][w1]
                if house + land <= v and area > result:
                    result = area

print(result)

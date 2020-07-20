# https://atcoder.jp/contests/abc079/tasks/abc079_d
H, W = list(map(int, input().split()))
C = []
for _ in range(10):
    row = list(map(int, input().split()))
    C.append(row)

number_count = {i: 0 for i in range(10)}
for _ in range(H):
    row = list(map(int, input().split()))
    for num in row:
        if num == -1:
            continue
        number_count[num] += 1

for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j] = min(C[i][j], C[i][k] + C[k][j])

# for row in C:
    # print(' '.join(map(str, row)))

# print(number_count)
result = 0
for k, v in number_count.items():
    result += C[k][1] * v

print(result)

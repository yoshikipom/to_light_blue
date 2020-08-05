# https://atcoder.jp/contests/joi2013ho/tasks/joi2013ho1

n = int(input())
A = list(map(int, input().split()))

# (1, 0が順番に続く長さ)
B = []
prev = A[0]
l = 1

for i in range(1, n):
    cur = A[i]
    if cur == prev:
        B.append(l)
        l = 1
    else:
        l += 1
    prev = cur

B.append(l)
# print(B)

result = 0
if len(B) <= 3:
    result = sum(B)
else:
    result = B[0] + B[1] + B[2]
    for i in range(3, len(B)):
        result = max(result, B[i-2] + B[i-1] + B[i])

print(result)

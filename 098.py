# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e

n = int(input())
A = list(map(int, input().split()))
MOD = 1000000007

counts = [0, 0, 0]
result = 1
for i in range(n):
    a = A[i]
    # print(a, counts, result)
    cnt = counts.count(a)
    result *= cnt
    result %= MOD
    for j in range(len(counts)):
        if counts[j] == a:
            counts[j] += 1
            break

print(result)

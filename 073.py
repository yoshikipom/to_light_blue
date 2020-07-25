# https://atcoder.jp/contests/abc145/tasks/abc145_d
import math
X, Y = list(map(int, input().split()))

if (X + Y) % 3 != 0:
    print(0)
    exit()


n = int((2*X - Y) // 3)
m = int((2*Y - X) // 3)

if n < 0 or m < 0:
    print(0)
    exit()


def comb(n, k):
    c = 1
    for i in range(k):
        c *= n - i
        c %= MOD
    d = 1
    for i in range(1, k + 1):
        d *= i
        d %= MOD
    return (c * pow(d, MOD - 2, MOD)) % MOD

MOD = 10 ** 9 + 7
result = comb(n+m, n)
print(result)

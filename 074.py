# https://atcoder.jp/contests/abc021/tasks/abc021_d
MOD = 10 ** 9 + 7


def comb(n, k):
    a = 1
    for i in range(k):
        a *= n-i
        a %= MOD
    b = 1
    for i in range(1, k + 1):
        b *= i
        b %= MOD
    return (a * pow(b, MOD - 2, MOD)) % MOD


n = int(input())
k = int(input())
print(comb(n-1+k, k))

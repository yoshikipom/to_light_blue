# https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_B

MOD = 10 ** 9 + 7
m, n = list(map(int, input().split()))
print(pow(m, n, MOD))

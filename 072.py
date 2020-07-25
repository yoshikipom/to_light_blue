# https://atcoder.jp/contests/abc034/tasks/abc034_c

import math

MOD = 10 ** 9 + 7

W, H = list(map(int, input().split()))

a = math.factorial((W - 1) + (H - 1))
b = math.factorial(H-1)
c = math.factorial(W-1)

print(a//(b*c) % MOD)

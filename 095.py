# https://atcoder.jp/contests/abc149/tasks/abc149_b

a, b, k = list(map(int, input().split()))

if k <= a:
    print(a - k, b)
elif a < k < a + b:
    print(0, b - (k-a))
else:
    print(0, 0)

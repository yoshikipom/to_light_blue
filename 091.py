# https://atcoder.jp/contests/abc144/tasks/abc144_d
import math

a, b, x = list(map(int, input().split()))
if a * a * b * (1/2) <= x:
    tmp = 2 * (a*a*b-x) / (a*a*a)
    print(math.degrees(math.atan(tmp)))
else:
    tmp = a*b*b / (2*x)
    print(math.degrees(math.atan(tmp)))

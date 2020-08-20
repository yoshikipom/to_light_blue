# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_d
m = int(input())
D = 0
S = 0
for _ in range(m):
    d, c = list(map(int, input().split()))
    D += c
    S += c * d
result1 = D - 1
result2 = (S-1)//9
# print(D)
# print(S)
print(result1+result2)

# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_C


def lcs(x, y):
    a = len(x)
    b = len(y)
    c1 = [0] * (b + 1)
    for i in range(a):
        c2 = c1[:]
        for j in range(b):
            if x[i] == y[j]:
                c1[j+1] = c2[j] + 1
            elif c1[j+1] < c1[j]:
                c1[j+1] = c1[j]
    return c1[-1]


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        x = input()
        y = input()
        print(lcs(x, y))

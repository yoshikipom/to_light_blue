# https://atcoder.jp/contests/arc054/tasks/arc054_b

if __name__ == "__main__":
    P = float(input())

    def f(x):
        return x + P * (2 ** -(x/1.5))

    e = 10**(-8)
    l = -100
    r = 100
    while r - l > e:
        c1 = (l * 2 + r) / 3
        c2 = (l + r * 2) / 3

        if f(c1) > f(c2):
            l = c1
        elif f(c1) < f(c2):
            r = c2
        else:
            break

    print(f(l) if l > 0 else P)

# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_B

if __name__ == "__main__":
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    result = 0
    for t in T:
        l = 0
        r = n - 1
        while l <= r:

            # print('t {} l {} r {}'.format(t, l, r))
            c = (l + r) // 2
            if t < S[c]:
                r = c - 1
                continue
            elif t == S[c]:
                result += 1
                break
            elif S[c] < t:
                l = c + 1
                continue
            raise Exception

    print(result)

# https://atcoder.jp/contests/abc128/tasks/abc128_c


def check_switch_on(S, btn, P):
    for i, s_row in enumerate(S):
        on_cnt = 0
        # print(s_row)
        for s in s_row:
            if btn[s-1]:
                on_cnt += 1
        if P[i] != on_cnt % 2:
            return False
    return True


if __name__ == "__main__":
    N, M = map(int, input().split())

    S = []
    for _ in range(M):
        l = list(map(int, input().split()))
        k = l[0]
        s_row = l[1:]
        S.append(s_row)

    P = list(map(int, input().split()))

    cnt = 0
    for bit in range(1 << N):
        btn = [False] * N
        for i in range(N):
            if bit & (1 << i):
                btn[i] = True
        if check_switch_on(S, btn, P):
            # print(btn)
            cnt += 1

    print(cnt)

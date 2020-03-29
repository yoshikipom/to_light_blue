# https://atcoder.jp/contests/abc106/tasks/abc106_b


def solve(N):
    result = 0
    for x in range(1, N+1, 2):
        divisor_cnt = 0
        # print('x: {}'.format(x))
        for i in range(1, x+1, 2):
            # print('i: {}'.format(i))
            if x % i == 0:
                divisor_cnt += 1
        if divisor_cnt == 8:
            result += 1

    return result


if __name__ == "__main__":
    N = int(input())
    print(solve(N))

# https://onlinejudge.u-aizu.ac.jp/problems/2013


def to_my_time_unit(time_str: str):
    hour, minute, second = map(int, time_str.split(sep=':'))
    return int(hour) * 60*60 + int(minute) * 60 + int(second)


def solve(n):
    A = [0 for _ in range(24 * 60 * 60+1)]
    for _ in range(n):
        start_str, end_str = input().split()
        start = to_my_time_unit(start_str)
        end = to_my_time_unit(end_str)
        A[start] += 1
        A[end] -= 1
    B = [0 for _ in range(24 * 60 * 60+1)]
    tmp = 0
    for i in range(24 * 60 * 60+1):
        tmp += A[i]
        B[i] = tmp
    print(max(B))


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        solve(n)

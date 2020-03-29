# https://atcoder.jp/contests/abc002/tasks/abc002_4


def canCreateGroup(d, People):
    for target in People:
        for i in People:
            if i not in d[target]:
                return False
    return True


if __name__ == "__main__":
    N, M = map(int, input().split())

    d = {}

    for i in range(N):
        d[i] = [i]

    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1

        d[x].append(y)
        d[y].append(x)

    result = 0
    for bit in range(1 << N):
        People = []
        cnt = 0
        for i in range(N):
            if bit & (1 << i):
                People.append(i)
                cnt += 1

        if canCreateGroup(d, People):
            result = max(result, cnt)

    print(result)

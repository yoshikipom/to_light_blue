# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d

if __name__ == "__main__":
    m = int(input())
    Constellation = []
    for _ in range(m):
        t = tuple(map(int, input().split()))
        Constellation.append(t)
    Vector = set()
    start = Constellation[0]
    for i in range(1, m):
        target = Constellation[i]
        v = (target[0] - start[0], target[1] - start[1])
        Vector.add(v)

    n = int(input())
    Pic = set()
    for _ in range(n):
        p = tuple(map(int, input().split()))
        Pic.add(p)

    result = (0, 0)
    # すべての点を始点としてチェックする
    for p in Pic:
        # 始点からベクトル分移動した先に点があるかチェック
        for v in Vector:
            target = (p[0] + v[0], p[1] + v[1])
            if target not in Pic:
                break
        else:
            result = (p[0] - start[0], p[1] - start[1])

    print(*result)

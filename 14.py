# https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b

if __name__ == "__main__":
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = float('inf')
    for bit in range(1 << N):
        use = []
        for i in range(N):
            if bit & (1 << i):
                use.append(i)
        if len(use) != K:
            continue

        cost = 0
        eye_height = A[0]

        for i in range(1, N):
            a = A[i]
            if a > eye_height:
                eye_height = a
                continue
            elif i in use:
                eye_height = eye_height + 1
                cost += eye_height - a

        # print(bin(bit))
        # print(use)
        # print('cost {}'.format(cost))

        result = min(result, cost)

    print(result)

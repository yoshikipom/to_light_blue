# https: // atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d

if __name__ == "__main__":
    N = int(input())
    S = input()

    result = 0
    for i in range(1000):
        password = str(i).zfill(3)

        cur = 0
        for c in S:
            if password[cur] == c:
                cur += 1
            if cur == 3:
                result += 1
                break

    print(result)

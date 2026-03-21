# solved by tele_boy
# The problem is from Luogu
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0]
    cnt = 0
    for i in range(1, n):
        curr = arr[i]
        res = arr[:i]
        for j in res:
            if j < curr:
                cnt += 1
        ans.append(cnt)
        cnt = 0
    print(*ans)
    return ans


if __name__ == "__main__":
    main()
for _ in range(int(input())):
    n, p = map(int, input().split())
    days = list(map(int, input().split()))

    sub = [days[i+1]-days[i]-1 for i in range(n-1)]
    result = 0
    days.append(days[-1]+1)
    sub.append(float('inf'))

    for i in range(n):
        day = 1
        p_rem = p

        for j in range(i, n):
            if sub[j] <= p_rem:
                day += sub[j] + 1
                p_rem -= sub[j]
            else:
                day += p_rem
                break

        result = max(result, day)

    print(f"#{_ + 1} {result}")

# 이거 시간초과 15개 테케 통과
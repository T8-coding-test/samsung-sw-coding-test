def maximize_profit(test_cases):
    results = []
    for t in range(len(test_cases)):
        N, prices = test_cases[t]
        max_price = 0
        profit = 0
        # 뒤에서부터 탐색
        for price in reversed(prices):
            if price > max_price:
                max_price = price
            else:
                profit += max_price - price
        results.append(profit)
    return results

# 입력 처리
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    test_cases.append((N, prices))
# print(test_cases)

# 결과 계산 및 출력
results = maximize_profit(test_cases)
for i, res in enumerate(results, 1):
    print(f"#{i} {res}")

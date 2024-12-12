T = int(input())        # 테스트 케이스 입력

for k in range(1, T+1):
    N = int(input())    # 예측할 일수 입력
    prices_per_day = list(map(int, input().split()))    # N일 간 예측한 가격 입력
    max_price = 0   # N일 중 최대 가격
    profit = 0  # 최대 이득 (출력값)

    for i in range(N-1, -1, -1):    # 역순으로 돌려, 가장 금액이 높은 시점에 팔 수 있도록 탐색
        if prices_per_day[i] > max_price:   
            max_price = prices_per_day[i]       

        else:    
            profit += max_price - prices_per_day[i]

    print(f'#{k} {profit}')
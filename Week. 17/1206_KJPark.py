T = 10      # 테스트 케이스 10개
building_view = []

for case in range(T):
    N = int(input())    # 건물의 갯수 입력
    Height = list(map(int, input().split()))    # 각 건물의 높이를 입력받음
    view = 0    # 조망권 확보된 세대수

    for i in range(2, N-2):
        max_both_sides = max(Height[i-2], Height[i-1], Height[i+1], Height[i+2])    # 임의의 건물은 주변 2개의 건물들보다 높이가 높은 경우, "조망권을 확보하였다"고 정의 가능
        if Height[i] > max_both_sides:
            view += Height[i] - max_both_sides
    
    building_view.append(view)

for k, view_result in enumerate(building_view, 1):
    print(f'#{k} {view_result}')
    
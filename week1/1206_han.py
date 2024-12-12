T = 10
results = []

for t in range(T):
    N = int(input().strip())
    buildings = list(map(int, input().strip().split()))

    total_view = 0

    for i in range(2, N - 2):
        # 양옆 2칸의 최대 높이
        max_surrounding = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        # 조망권 확보된 세대 수
        if buildings[i] > max_surrounding:
            total_view += buildings[i] - max_surrounding

    # 결과 저장
    results.append(total_view)

# 결과 출력
for i, res in enumerate(results, 1):
    print(f"#{i} {res}")
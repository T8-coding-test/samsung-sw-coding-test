T = int(input())
for i in range(1, T+1):
    N = int(input())
    K = int(input())
    camera_positions = list(map(int, input().split()))
    camera_positions = sorted(set(camera_positions))

    if len(camera_positions) <= K:  # 카메라가 수신기보다 적은 경우
        print(f"#{i} 0")
        continue

    # 인접한 카메라 좌표 간의 거리 계산
    distances = []
    for idx in range(1, len(camera_positions)):
        distances.append(camera_positions[idx] - camera_positions[idx-1])

    # 가장 큰 거리부터 K-1개를 제거하여 K개의 그룹을 만듦
    distances.sort(reverse=True)
    for _ in range(K-1):
        distances.pop(0)

    # 남은 거리들의 합이 최소 길이의 합
    print(f"#{i} {sum(distances)}")

T = int(input())

for test_case in range(1, T+1):
    # N(단속 카메라 갯수), K(수신기 갯수) 및 단속 카메라 좌표 받음
    N = int(input())
    K = int(input())
    positions = list(map(int, input().split()))
    
    # 받은 카메라 좌표 정렬
    positions.sort()
    
    # 카메라 좌표 사이의 간격 계산
    gaps = [positions[i+1] - positions[i] for i in range(1, N)]
    
    # 간격 정렬
    gaps.sort()
    
    # 간격 출력 중 최솟값 출력
    min_length = sum(gaps[:N-K] if N > K else 0)
    
    # min_length 출력
    print(f"#{test_case} {min_length}")
    
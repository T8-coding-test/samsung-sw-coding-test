T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    K = int(input())
    coord = list(map(int, input().split()))
    
    if N <= K:
        print(f"#{test_case} 0")
        continue
    
    coord.sort()
    gap = []
    for i in range(1, N):
        gap.append(coord[i] - coord[i - 1])
    
    gap.sort(reverse=True)
    for _ in range(K - 1):
        gap.pop(0)
    
    # 남은 간격 합 계산
    result = sum(gap)
    
    # 결과 출력
    print(f"#{test_case} {result}")
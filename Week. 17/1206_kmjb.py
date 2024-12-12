T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))
    rtv = 0
    for i in range(2, N - 2):
        max_height = max([heights[i-2], heights[i-1], heights[i+1], heights[i+2]])
        if heights[i] > max_height:
            rtv += heights[i] - max_height
    print(f"#{test_case} {rtv}")
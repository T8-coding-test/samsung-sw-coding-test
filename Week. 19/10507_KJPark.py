T = int(input())

for test_case in range(1, T + 1):
    n, p = list(map(int, input().split()))
    n_list = list(map(int, input().split()))
    
    # 슬라이딩 윈도우로 연속된 구간 확인
    left = 0    # 왼쪽 끝
    max_length = 1  # 최대 연속 기간
    
    for right in range(n):
        while n_list[right] - n_list[left] - (right - left) > p:
            left += 1
        max_length = max(max_length, right - left + 1)
    
    print(f'#{test_case} {max_length+p}')

# # 아래는 런타임 에러 코드
# T = int(input())
# n_list = []

# for test_case in range(1, T + 1):
#     n, p = list(map(int, input().split()))
#     n_list.append(list(map(int, input().split())))
    
#     # 슬라이딩 윈도우로 연속된 구간 확인
#     left = 0    # 왼쪽 끝
#     max_length = 1  # 최대 연속 기간
    
#     for right in range(n):
#         while n_list[right] - n_list[left] - (right - left) > p:
#             left += 1
#         max_length = max(max_length, right - left + 1)
    
#     print(f'#{test_case} {max_length+p}')
    
# # 런타임 에러 코드 - 2
# T = int(input())

# for test_case in range(1, T + 1):
#     n, p = list(map(int(input().split())))
#     n_list = list(map(int, input().split()))
    
#     # 슬라이딩 윈도우로 연속된 구간 확인
#     left = 0    # 왼쪽 끝
#     max_length = 1  # 최대 연속 기간
    
#     for right in range(n):
#         while n_list[right] - n_list[left] - (right - left) > p:
#             left += 1
#         max_length = max(max_length, right - left + 1)
    
#     print(f'#{test_case} {max_length+p}')
    
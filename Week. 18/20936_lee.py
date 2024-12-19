"""
다 못했습니다
"""

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    box_nums = list(map(int, input().split()))
    box_nums.append(0)
    
    cursor = N
    result = []
    
    for value in range(1, N+1):
        if box_nums[value-1] == value:
            continue
        tar_idx = box_nums.index(value)
        result.append(tar_idx+1)
            
        box_nums[tar_idx], box_nums[cursor] = box_nums[cursor], box_nums[tar_idx]
        cursor = tar_idx 

        
    print(len(result))
    print(" ".join(map(str, result)))
        
        
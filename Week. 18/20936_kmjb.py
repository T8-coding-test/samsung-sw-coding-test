T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    K = 0

    seq = []
    box = list(map(int, input().split()))
    box_set = set(box)
    box.append('X')  

    while True:
        empty_idx = box.index('X')
        empty_num = empty_idx + 1

        if empty_num in box_set:  
            target_idx = box.index(empty_num)
            K += 1
            seq.append(target_idx + 1)
            box[target_idx], box[empty_idx] = box[empty_idx], box[target_idx]

        else: 
            misplaced = False
            for i in range(len(box) - 1):
                if box[i] != i + 1:  
                    box[i], box[empty_idx] = box[empty_idx], box[i]
                    K += 1
                    seq.append(i + 1)
                    misplaced = True
                    break

            if not misplaced:
                print(K)
                if seq:
                    print(*seq)
                break
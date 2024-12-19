T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    N_num = list(map(int, input().split()))
    
    # 결과 저장 리스트
    moves = []
    
    # 현재 상태를 나타내는 배열
    boxes = N_num + ['X']
    
    for i in range(N):
        # i번 상자의 현재 위치
        current_pos = boxes.index(i)
        
        # i번 상자를 i번 칸으로 이동
        while current_pos != i:
            empty_pos = boxes.index('X')
            
            # i번 상자를 빈 칸으로 옮기기
            boxes[current_pos], boxes[empty_pos] = boxes[empty_pos], boxes[current_pos]
            moves.append(current_pos)
            
            # 현재 상자 위치번호 업데이트
            current_pos = boxes.index(i)
    
    # 결과 출력
    print(len(moves))
    print(" ".join(map(str, moves)))
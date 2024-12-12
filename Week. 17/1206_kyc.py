for num in range(10):
    n = int(input())
    apt = list(map(int, input().split()))
    
    def cal(curser):
        if curser > n - 3:
            return 0
        temp = [apt[curser] - apt[curser - 2], apt[curser] - apt[curser - 1], apt[curser] - apt[curser + 1], apt[curser] - apt[curser + 2]]
        if any(t < 0 for t in temp):
            curser += 1
        elif any(t == 0 for t in temp):
            curser += 3
        else:
            min_val = min(temp)
            curser += 3
            return min_val + cal(curser)
        return cal(curser)
    
    print(f"#{num + 1} {cal(2)}")
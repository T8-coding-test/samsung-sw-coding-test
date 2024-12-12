T = 10

for test_case in range(1, T + 1):
    N = int(input())
    build = list(map(int, input().split()))
    
    result = 0
    
    for i in range(2, N-2):
        surround_max = max(build[i-2], build[i-1], build[i+1], build[i+2])
        
        if build[i] > surround_max:
            result = result + build[i] - surround_max
    
    print("#{} {}".format(test_case, result))
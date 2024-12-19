T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    K = int(input())
    locations = list(set(map(int, input().split())))
    
    if K >= len(locations):
        result = 0
        print("#{} {}".format(test_case, result))
        continue
    
    locations.sort()
        
    each_len = []
    
    for i in range(len(locations)-1):
        sub = locations[i+1] - locations[i]
        each_len.append(sub)
        
    if K == 1:
        print("#{} {}".format(test_case, max(locations)-min(locations)))
        continue
        
        
    each_len.sort()
    
    result = sum(each_len[:-K+1])
        
    print("#{} {}".format(test_case, result))
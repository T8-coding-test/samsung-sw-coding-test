'''
시간초과 -> 11개 맞음..
'''


from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, p = map(int, input().split())
    date = list(map(int, input().split(" ")))
    
    point = 0
    result = []
    
    while point < len(date):
        tries= 0
        temp = []
        deq = deque(date[point:])
        temp.append(deq.popleft())
        
        while deq:
            if deq[0] == temp[-1]+1:
                temp.append(deq.popleft())
            else:
                if tries < p:
                    temp.append(temp[-1]+1)
                    tries+=1
                else:
                    break
    
        each_result = len(temp)
        result.append(each_result)
        point +=1
             
    
    print("#{} {}".format(test_case, max(result)))
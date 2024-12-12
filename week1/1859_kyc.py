from collections import deque
 
for _ in range(int(input())):
    n = int(input())
    price = list(map(int, input().split()))
    result = -sum(price)
 
    d = deque()
 
    d.append([price[0], 0])
 
    for i in range(1, n):
        while True:
            temp = d.pop()
             
            if temp[0] > price[i]:
                d.append(temp)
                d.append([price[i], i])
                break
            elif len(d) == 0 or temp[0] == price[i]:
                d.append([price[i], i])
                break
 
    l = -1
 
    while len(d) != 0:
        temp = d.popleft()
        result += temp[0] * (temp[1] - l)
        l = temp[1]
     
    print(f"#{_+1} {result}")
# import numpy as np

T = int(input())

for test_case in range(1, T + 1):
    day = int(input())
    price = list(map(int, input().split()))
    
    result = 0
    
    while True:
        max_price = max(price)
        idx_max = price.index(max_price)
        total = idx_max * price[idx_max]
        sub = sum(price[:idx_max])
        result = result + total - sub
        
        if idx_max == len(price) - 1:
            break
        
        price = price[idx_max+1:]     
    
    print("#{} {}".format(test_case, result))
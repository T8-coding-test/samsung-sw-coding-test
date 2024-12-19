for _ in range(int(input())):
    n = int(input())
    k = int(input())
    l = list(map(int, input().split()))
    l = list(set(l))
    l.sort()
    if len(l) <= k:
        print(f"#{_+1} 0")
        continue
     
    count = len(l) - k
    check = [0 for _ in range(len(l)-1)]
    for i in range(len(l)-1):
        check[i] = abs(l[i+1]-l[i])
 
    check.sort()
    print(f"#{_+1} {sum(check[:count])}")
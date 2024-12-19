for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ls = [i for i in l]
    ls.sort()
    
    if l == ls:
        print(0)
        print()
        continue
    
    l.append(n+1)
    for i in range(len(l)):
        l[i] -= 1
    
    d = {l[i]: i for i in range(n + 1)}
    result = []

    for i in range(n+1):
        if d[i] != i:
            d[n], d[i] = d[i], d[n]
            result.append(d[n])
            break
    
    while True:
        if d[n] == n:
            sw = True
            for i in range(n+1):
                if d[i] != i:
                    d[n], d[i] = d[i], d[n]
                    result.append(d[n])
                    sw = False
                    break
            if sw:
                break
        temp = d[n]
        d[n], d[temp] = d[temp], d[n]
        result.append(d[n])

    print(len(result))
    for i in result:
        print(i+1, end=" ")
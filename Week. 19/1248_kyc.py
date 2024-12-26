from collections import deque

for _ in range(int(input())):
    V, E, a, b = map(int, input().split())
    element = list(map(int, input().split()))

    tree = {i:i for i in range(V+1)}
    rev_tree = {i:[] for i in range(V+1)}

    for i in range(E):
        tree[element[2*i+1]] = element[2*i]
        rev_tree[element[2*i]].append(element[2*i+1])

    def find_parent(a):
        result = []
        find = a
        while tree[find] != find:
            result.append(find)
            find = tree[find]
        result.append(find)
        return result
    
    sub_a = find_parent(a)
    sub_b = find_parent(b)

    cont = -1
    
    while sub_a[cont] == sub_b[cont]:
        cont -= 1

    common = sub_a[cont + 1]

    d = deque(rev_tree[common])

    res = 1
    while len(d) != 0:
        temp = d.popleft()
        res += 1
        for i in rev_tree[temp]:
            d.append(i)
    
    print(f"#{_+1} {common} {res}")
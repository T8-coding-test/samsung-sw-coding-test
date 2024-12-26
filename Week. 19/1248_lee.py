T = int(input())
for test_case in range(1, T + 1):
    V, E, target1, target2 = map(int, input().split(" "))
    user_input = list(map(int, input().split(" ")))
    
    tree = [[] for _ in range(V+1)]
    each_parent = [-1] * (V+1)
    
    for i in range(0, len(user_input), 2):
        parent, child = user_input[i], user_input[i+1]
        tree[parent].append(child)
        each_parent[child] = parent
        
    path_one = []
    path_two = []
    
    one, two = target1, target2
    
    while one != -1:
         path_one.append(one)
         one = each_parent[one]
    
    while two != -1:
         path_two.append(two)
         two = each_parent[two]
    
    path_one = path_one[::-1]
    path_two = path_two[::-1]
    
    i = 0
    while i < len(path_one) and i < len(path_two) and path_one[i] == path_two[i]:
        i += 1
    common_target = path_one[i - 1] 
    
    visited = [False] * (V + 1)
    
    def tree_size(common):
        visited[common] = True
        result = 1
        
        for child in tree[common]:
            if not visited[child]:
                result += tree_size(child)
        return result
    
    final = tree_size(common_target)
    
    print("#{} {} {}".format(test_case, common_target, final))
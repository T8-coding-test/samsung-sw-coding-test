# 더 수정 필요


T = int(input())

limit = 540

for test_case in range(1, T + 1):
    N, M = map(int, input().split(" "))
    
    inf = float('inf')
    times = [[inf] * N for _ in range(N)]
    for i in range(N):
        times[i][i] = 0
    
    for i in range(N-1):
        temp = list(map(int, input().split(" ")))
        for j, time in enumerate(temp):
            val = i+j+1
            times[i][val] = time
            times[val][i] = time
    
    each_type = [None]*N
    play_time = [0]*N
    score = [0]*N
    
    airport = -1
    hotels = []
    
    for i in range(N):
        information = input().split(" ")
        j = information[0]
        each_type[i]=j
        
        if j == 'A':
            airport = i
        elif j == 'H':
            hotels.append(i)
        else:
            play = int(information[1])
            rating = int(information[2])
            play_time[i] = play
            score[i] = rating
    
    best_score = 0
    route_list = []
    
    def dfs(day, now_loc, used_time, visited, total_score, route):
        global best_score, route_list
         
        if day == M-1:
            go_air_dis = times[now_loc][airport]
            if used_time + go_air_dis <= limit:
                final_score = total_score
                final_route = route + [airport]
                 
                if final_score > best_score:
                    best_score = final_score
                    route_list = final_route.copy()
             
            return
        
        
        for j in range(N):
            if each_type[j] == 'P' and j in visited:
                continue
            
            travel_time = times[now_loc][j]
            if each_type[j] == 'P':
                run_time = play_time[j]
            else:
                run_time = 0
            
            need_time = travel_time+run_time
        
            if used_time + need_time <= limit:
                new_visited = visited.copy()
                each_score = 0
                
                if each_type[j] == 'P':
                    new_visited.add(j)
                    each_score = score[j]
                
                dfs(day, j, used_time+need_time, new_visited, total_score+each_score, route+[j])

        
        for h in hotels:
            travel_time = times[now_loc][h]
            if used_time + travel_time <= limit:
                dfs(day+1, h, 0, visited.copy(), total_score, route+[h])
    
    dfs(day=0, now_loc=airport, used_time=0, visited=set(), total_score=0, route=[airport])
    
    result_path = [str(p+1) for p in route_list]
    print("#{} {}".format(test_case, " ".join(result_path)))     
         
         
            
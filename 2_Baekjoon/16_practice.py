def get_max(idx, cur_sum): # 
    global max_sum
    if idx == 11: ## max_sum를 비교하며 계속 바꾸어 주는 곳이다.
        if cur_sum > max_sum:
            max_sum = cur_sum
        return # 함수 끝

    for j in range(11): ## 11번을 반복한다. 모든 경우의 수가 반복이 되는 구간이다.
        if check[j]: continue # 중간에 방문한 곳이면 그냥 넘어가도록 잡아주는 곳
        
        if sportsman[idx][j]: #0이 아닌 이상 다음의 조건문을 실행한다. 
            check[j] = 1 # 다음재귀의 반복을 더이상 하지 않도록 1을 선언(조건문을 위해서)
            
            get_max(idx+1, cur_sum+sportsman[idx][j])
            
            check[j] = 0


T = int(input()) # 입력

for _ in range(T): # 그만큼 반복
    sportsman = [] # 배열 초기화
    check = [0] * 11 # check를 11개 만든다.
    max_sum = 0 
    for i in range(11): #11번 입력을 받는다. 
        sportsman.append(list(map(int, input().split())))
    get_max(0, 0) # 함수 호출

    print(max_sum)
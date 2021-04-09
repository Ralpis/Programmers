answer = 0
#DFS로 타겟넘버까지 도달한 갯수를 저장해서 최종 출력을 목표
def dfs (numbers, n, target, hap):
    global answer
    if( n == len(numbers)-1):
        if((hap+numbers[n])==target)or((hap-numbers[n])==target):
            answer+=1
    else:
        dfs(numbers, n+1,target,hap+numbers[n]);
        dfs(numbers, n+1,target,hap-numbers[n]);
    return answer;

def solution(numbers, target):
    dfs(numbers, 0, target, 0)
    return answer
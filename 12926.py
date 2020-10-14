#12926 시저암호
#https://programmers.co.kr/learn/courses/30/lessons/12926


def solution(s, n):
    #65~90 , 97~122
    answer =''
    for i in s:
        tmp = ord(i)+n
        if i == ' ':
            answer+=i
        elif 64<ord(i)<91:
            if tmp>90:
                answer += chr(tmp-26)
            else:
                answer += chr(tmp)
        elif 96<ord(i)<123:
            if tmp>122:
                answer += chr(tmp-26)
            else:
                answer += chr(tmp)
    
    return answer

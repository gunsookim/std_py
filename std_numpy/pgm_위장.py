def solution(clothes):
    answer = 1
    op = list(set([i[1] for i in clothes]))
    for i in op:
        tmp = [clothes[j][0] for j in range(len(clothes)) if clothes[j][1] == i]
        answer *= (len(tmp)+1)
    return answer - 1
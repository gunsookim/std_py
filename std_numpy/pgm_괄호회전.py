def solution(s):
    answer = 0
    tmp = list(s)[:]
    for i in range(len(tmp)):
        tmp.append(tmp[0])
        tmp.pop(0)
        arr = ''.join(tmp)
        for j in range(len(tmp)//2):
            arr = arr.replace('[]', '').replace('()', '').replace('{}', '')
        if len(arr) == 0:
            answer +=1
    return answer


solution("[)(]")
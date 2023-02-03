def solution(dirs):
    answer = 0
    d = list(dirs)
    memory = []
    pos = [0, 0]
    pos_set = {'U': [0,1], 'D': [0,-1], 'R': [1,0],'L': [-1,0]}
    for i in range(len(d)):
        tmp = [0, 0]
        tmp[0] = pos[0] + pos_set[d[i]][0]
        tmp[1] = pos[1] + pos_set[d[i]][1]
        if ((tmp[0] <= 5) and  (tmp[0] >= -5)) and ((tmp[1] <= 5) and (tmp[1] >= -5)):
            memory.append([tuple(pos), tuple(tmp)])
            pos[0] = tmp[0]
            pos[1] = tmp[1]
    a = [sorted(memory[i]) for i in range(len(memory))]
    arr = list(map(tuple, a))
    answer = len(set(arr))
    return answer

solution("ULURRDLLU")
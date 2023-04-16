def solution(genres, plays):
    answer = []
    d = dict.fromkeys(genres, 0)
    for i in range(len(genres)):
        d[genres[i]] += plays[i]
    d = sorted(d.items(), key = lambda x:x[1], reverse = True)
    arr = []
    for i in d:
        tmp = [plays[j] for j in range(len(genres)) if i[0] == genres[j]]
        arr += sorted(tmp, reverse=True)[:2]
    for i in arr:
        if i in plays:
            answer.append(plays.index(i))
            plays[plays.index(i)] = 0
    return answer
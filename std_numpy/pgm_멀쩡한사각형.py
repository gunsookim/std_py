def solution(w,h):
    answer = 1
    size = [0,0]
    gcm = 1
    for i in reversed(range(1, w+1 if w >= h else h+1)):
        if (not w % i) and (not h % i):
            gcm = i
            break
    size[0] = w//gcm
    size[1] = h//gcm
    answer = w*h - (size[0]+size[1]-1)*gcm
    return answer

solution(8, 12)

def solution(s):
    cnt = []
    for i in s:
        if i == '(':
            cnt.append(i)
        elif i == ')':
            if len(cnt) == 0:
                return False
            cnt.pop(-1)
    return len(cnt) == 0
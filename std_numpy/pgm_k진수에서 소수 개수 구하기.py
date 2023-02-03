import math

def check(n):
    if n != 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n%i == 0:
                print(i)
                return False
        return True

def solution(n, k):
    answer = -1
    print(n, k)
    num = ''
    while n:
        num = str(n%k) + num
        n //= k
    num = [int(i) for i in num.split('0', ) if i != '' and check(int(i))]
    print(num)

    """
    arr = [True]*(max(num)+1)
    print(max(num))
    res = []
    arr[0], arr[1] = False, False
    for i in range(2, int(math.sqrt(max(num)))+1):
        if arr[i] and (i in num):
            print(i)
            res.append(i)
            j = 2
            while i*j <= max(num):
                arr[i*j] = False
                j += 1
    print(res)
    res = [a for a in num if arr[a]]
    print(res)
    check = [[j for j in range(2, i + 1) if i%j == 0 and j in res] for i in num]
    print(check)
    answer = len(sum(check, []))
    print(answer)
    """
    return answer

solution(437674,3)
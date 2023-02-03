def solution(n, left, right):
    l = n*n
    print(l, left//n, right//n, left%n, right%n)
    a = [i + 1 if j <= i else j + 1 for j in range(n) for i in range(n)][left:right + 1]
    print(a)
    answer = [i%n+1 if i%n >= i//n else i//n+1  for i in range(left, right+1)]
    print(answer)
    arr = [[i+1 if j<=i else j+1 for j in range(n)] for i in range(n)] #[left:right+1]
    [print(arr[i]) for i in range(n)]
    """ 
    전체길이 = n*n = len(answer)
    left: a*n + b ~ right: x*n + y
    i*n + j
    """
    return arr

solution(4, 7, 14)
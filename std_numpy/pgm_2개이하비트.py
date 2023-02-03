def solution(numbers):
    answer = []
    """
    for i in numbers:
        max_num = int(''.join(['1']*(len(bin(i))-1)), 2)
        print(bin(max_num)[2:])
        m = '1'+bin(i)[2:]
        print(m)
        for j in range(i + 1, max_num):
            if bin(j^i).count('1') <= 2:
                answer.append(j)
                break
    print(answer)"""

    """
        max_num = list('0' + ''.join(bin(i)[2:]))
        idx = ''.join(max_num).rfind('0')
        max_num[idx] = '1'
        if i%2 == 1:
            max_num[idx + 1] = '0'
        answer.append(int(''.join(max_num), 2))
    print(answer)
    return answer
    """
    return [((i ^ (i + 1)) >> 2) + i + 1 for i in numbers]


print(solution([2,7]))
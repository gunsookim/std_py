def solution(fees, records):
    print(records)

    num_car = dict.fromkeys(sorted(list(set([i[6:10] for i in records]))), 0)
    print(num_car)

    tmp = ' '.join(records)
    print(tmp)
    for i in num_car:
        if tmp.count(i)%2:
            max_t = "23:59 " + i + " OUT"
            print(max_t)
            records.append(max_t)
    records.sort(key=lambda x:x[6:10], reverse=False)
    print(records)

    for record in records:
        time, num, state = record.split()
        h, m = map(int, time.split(':'))
        t = h*60 + m
        if state == 'IN':
            num_car[num] -= t
        else:
            num_car[num] += t
    print(num_car)

    """
    answer = [fees[1] if num_car[val] <= fees[0] else fees[1] + fees[3]*((num_car[val] - fees[0])//fees[2] + 1) 
              for idx, val in enumerate(num_car)]
    """
    answer = [0]*len(num_car)
    for idx, val in enumerate(num_car):
        if num_car[val] <= fees[0]:
            answer[idx] = fees[1]
        else:
            gap = num_car[val] - fees[0]
            if gap%fees[2] == 0:
                answer[idx] = fees[1] + fees[3]*(gap//fees[2])
            else:
                answer[idx] = fees[1] + fees[3]*(gap//fees[2] + 1)

    print(answer)

    return answer


# Test case
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
fees = [120, 0, 60, 591]
print(solution(fees, records))  # Output: [3, 3]

"""
차번호 정렬
IN, OUT 수 체크
"""


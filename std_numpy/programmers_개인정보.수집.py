def solution(today, terms, privacies):
    t_day = list(map(int, today.split('.')))
    day = (t_day[0]*12 + t_day[1])*28 + t_day[2]
    t_list = [(str(terms[i].split()[0]), int(terms[i].split()[1])) for i in range(len(terms))]
    t_l = dict(t_list)
    check_day = [list(privacies[i].split()) for i in range(len(privacies))]
    c_day = []
    for i in range(len(check_day)):
        c = list(map(int, check_day[i][0].split(".")))
        c_day.append((c[0] * 12 + c[1]) * 28 + c[2] + t_l[check_day[i][1]]*28)
    answer = [i+1 for i in range(len(c_day)) if c_day[i]<=day]

    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])